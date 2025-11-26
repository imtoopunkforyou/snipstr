import pytest

from snipstr.errors import (
    SnipSideError,
    SnipSizeIsNotIntError,
    SnipSizeIsNotPositiveIntError,
)
from snipstr.snipstr import SnipStr


def test_size_is_not_int(long_text, not_int):
    s = SnipStr(long_text)
    with pytest.raises(SnipSizeIsNotIntError):
        s.snip_to(not_int)


def test_size_is_not_positive_int(negative_int, long_text):
    s = SnipStr(long_text)
    with pytest.raises(SnipSizeIsNotPositiveIntError):
        s.snip_to(negative_int)


def test_snip_side(long_text, not_side):
    s = SnipStr(long_text)
    with pytest.raises(SnipSideError):
        s.by_side(not_side)
