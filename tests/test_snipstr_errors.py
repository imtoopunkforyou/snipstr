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


def test_snip_side(long_text):
    """Test that invalid side values raise SnipSideError."""
    s = SnipStr(long_text)

    # Test with invalid string value
    with pytest.raises(SnipSideError) as exc_info:
        s.by_side('invalid_side')
    assert 'invalid_side' in str(exc_info.value)

    # Test with invalid type (not str or Sides enum)
    with pytest.raises(SnipSideError) as exc_info:
        s.by_side(123)
    assert '123' in str(exc_info.value)
