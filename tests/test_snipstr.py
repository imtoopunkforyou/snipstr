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
