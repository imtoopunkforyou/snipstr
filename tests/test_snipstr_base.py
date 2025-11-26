from snipstr.enums import Sides
from snipstr.snipstr import SnipStr


def test_source(source):
    s = SnipStr(source)
    assert s.source == source


def test_comparable(long_text, very_long_text):
    s = SnipStr(long_text)
    s_2 = SnipStr(very_long_text)

    s.snip_to(10).by_side('left')
    s_2.snip_to(5).with_replacement_symbol()

    assert s > s_2
    assert s >= s_2
    assert s_2 <= s
    assert s_2 < s


def test_hashed(long_text):
    s = SnipStr(long_text)
    s_2 = SnipStr(long_text)
    assert s == s_2
    assert hash(s) == hash(s_2)

    s.snip_to(10)
    s_2.snip_to(10)
    assert s == s_2
    assert hash(s) == hash(s_2)

    s.by_side('left')
    assert s != s_2
    assert hash(s) != hash(s_2)
    s_2.by_side('left')
    assert s == s_2
    assert hash(s) == hash(s_2)

    s.with_replacement_symbol()
    assert s != s_2
    assert hash(s) != hash(s_2)
    s_2.with_replacement_symbol()
    assert s == s_2
    assert hash(s) == hash(s_2)

    s.snip_to(11)
    assert s != s_2
    assert hash(s) != hash(s_2)
    s_2.snip_to(11)
    assert s == s_2
    assert hash(s) == hash(s_2)

    assert len({s, s_2}) == 1


def test_repr():
    long_text = (
        'Python source code and installers are'
        ' available for download for all versions!'
    )
    small_text = 'lol'
    long_s = SnipStr(long_text)
    small_s = SnipStr(small_text)

    assert repr(long_s) == (
        'SnipStr(source=Python sou <...>  versions!, length=78, '
        'side=right, replacement_symbol=(None,))'
    )
    assert repr(small_s) == (
        'SnipStr(source=lol, length=3, side=right, replacement_symbol=(None,))'
    )


def test_comparable_not_implemented(long_text):
    s = SnipStr(long_text)

    result = s.__lt__('not a SnipStr')
    assert result is NotImplemented

    result = s.__le__(123)
    assert result is NotImplemented

    result = s.__gt__([])
    assert result is NotImplemented

    result = s.__ge__(None)
    assert result is NotImplemented


def test_eq_not_implemented(long_text):
    s = SnipStr(long_text)

    result = s.__eq__('not a SnipStr')
    assert result is NotImplemented

    result = s.__eq__(123)
    assert result is NotImplemented

    result = s.__eq__([])
    assert result is NotImplemented


def test_cut_back_with_left_side(long_text, length):
    s = SnipStr(long_text)
    s.snip_to(length).by_side(Sides.LEFT)
    # Ensure _side is LEFT
    assert s._side == Sides.LEFT.value

    # Call _build which internally calls _cut_back
    result = str(s)
    # Should take last TEST_LENGTH characters
    assert len(result) == length
    assert result == str(long_text)[-length:]


def test_add_replacement_symbol_with_left_side(long_text, length):
    s = SnipStr(long_text)
    symbol = '...'
    s.snip_to(length).by_side(Sides.LEFT).with_replacement_symbol(symbol)

    # Ensure conditions are met
    assert s._side == Sides.LEFT.value
    assert s._replacement_symbol == symbol

    # Call _build which internally calls _add_replacement_symbol
    result = str(s)
    assert len(result) == length
    # With LEFT side, symbol should be at the start
    assert result.startswith(symbol)


def test_cut_back_elif_branch_not_taken(long_text, length):
    s = SnipStr(long_text)
    s.snip_to(length)
    s._side = 'invalid'

    result = str(s)
    assert s._lenght == length
    assert len(result) == len(str(long_text))


def test_add_replacement_symbol_elif_branch_not_taken(long_text, length):
    s = SnipStr(long_text)
    symbol = '...'
    s.snip_to(length).with_replacement_symbol(symbol)
    s._side = 'invalid'

    assert s._replacement_symbol == symbol

    result = str(s)
    assert s._lenght == length
    assert len(result) == len(str(long_text))
