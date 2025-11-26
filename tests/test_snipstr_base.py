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
