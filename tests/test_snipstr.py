from snipstr.constants import Sides
from snipstr.snipstr import SnipStr


def test_snipstr(long_text):
    max_len = 10
    s = SnipStr(long_text)
    s.snip_to(max_len).by_side(Sides.LEFT).with_replacement_symbol()

    assert str(s).startswith('...')
    assert len(str(s)) < len(long_text)
    assert len(str(s)) == max_len
    assert len(s) == len(str(s))


def test_snipstr_w_replacement_symbol(long_text):
    symbol = '<...>'
    s = SnipStr(long_text).with_replacement_symbol(symbol)
    assert symbol in str(s)


def test_create_snipstr_without_sides_enum(long_text):
    max_len = 10
    s = SnipStr(long_text)

    s.by_side('left').with_replacement_symbol().snip_to(max_len)
    assert len(str(s)) == max_len
    assert str(s).startswith('...')

    s.by_side('right').with_replacement_symbol().snip_to(max_len)
    assert len(str(s)) == max_len
    assert str(s).endswith('...')


def test_snipstr_w_default_right_side(long_text):
    max_len = 10
    s = SnipStr(long_text).snip_to(max_len).with_replacement_symbol()
    assert len(str(s)) == max_len
    assert str(s).endswith('...')
