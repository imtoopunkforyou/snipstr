import pytest

from snipstr.enums import Sides
from snipstr.snipstr import SnipStr


@pytest.mark.parametrize('side', [Sides.LEFT, Sides.RIGHT])
def test_snipstr(long_text, side):
    max_len = 10
    s = SnipStr(long_text)
    s.snip_to(max_len).by_side(side).with_replacement_symbol()

    assert len(str(s)) < len(long_text)
    assert s._side == side.value
    assert len(str(s)) == max_len
    assert len(s) == len(str(s))


def test_snipstr_w_replacement_symbol(long_text):
    symbol = '<...>'
    s = SnipStr(long_text).with_replacement_symbol(symbol)

    assert symbol in str(s)


@pytest.mark.parametrize('side', [Sides.LEFT.value, Sides.RIGHT.value])
def test_create_snipstr_without_sides_enum(long_text, side):
    max_len = 10
    s = SnipStr(long_text)

    s.by_side(side).with_replacement_symbol().snip_to(max_len)
    assert len(str(s)) == max_len

    s.by_side(side).with_replacement_symbol().snip_to(max_len)
    assert len(str(s)) == max_len


def test_snipstr_w_default_right_side_and_default_replacement_symbol(long_text):
    max_len = 10
    s = SnipStr(long_text).snip_to(max_len).with_replacement_symbol()

    assert len(str(s)) == max_len
    assert str(s).endswith('...')


def test_snipstr_with_left_side_and_replacement_symbol(long_text):
    """Test LEFT side with replacement symbol to cover branch 138->141."""
    max_len = 10
    symbol = '...'
    s = SnipStr(long_text)
    s.snip_to(max_len).by_side(Sides.LEFT).with_replacement_symbol(symbol)

    result = str(s)
    assert len(result) == max_len
    assert s._side == Sides.LEFT.value
    assert s._replacement_symbol == symbol
    # With LEFT side, replacement symbol should be at the start
    assert result.startswith(symbol)


def test_snipstr_without_replacement_symbol(long_text):
    """Test without replacement symbol to cover branch 134->141."""
    max_len = 10
    s = SnipStr(long_text)
    s.snip_to(max_len).by_side(Sides.RIGHT)
    # Don't call with_replacement_symbol, so it stays empty

    assert len(str(s)) == max_len
    assert s._replacement_symbol == ''
    # String should be cut but without replacement symbol
    assert len(str(s)) <= max_len


def test_snipstr_with_left_side_cut_back(long_text):
    """Test LEFT side cut_back to cover branch 128->131."""
    max_len = 10
    s = SnipStr(long_text)
    s.snip_to(max_len).by_side(Sides.LEFT)
    # Don't set replacement_symbol to test the elif branch in _cut_back

    result = str(s)
    assert len(result) == max_len
    assert s._side == Sides.LEFT.value
    # Should take last max_len characters when no replacement symbol
    assert result == str(long_text)[-max_len:]
