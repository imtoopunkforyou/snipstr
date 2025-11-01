from typing import Annotated, Any, Literal, TypeAlias, TypeVar, final

import annotated_types

from snipstr.comparison import ComparableByLength
from snipstr.errors import (
    SnipSideError,
    SnipSizeIsNotIntError,
    SnipSizeIsNotPositiveIntError,
)

SnipSide: TypeAlias = Literal['left', 'right']
SelfSnipStr = TypeVar('SelfSnipStr', bound='SnipStr')
SnipStrInstance = TypeVar('SnipStrInstance', bound='SnipStr')

PositiveInt = Annotated[int, annotated_types.Gt(0)]

@final
class SnipStr(ComparableByLength):
    """A string-like object that can be truncated with configurable options.

    SnipStr wraps any object and provides functionality to truncate its string
    representation to a specified length. It supports truncation from either
    the left or right side, and optional ellipsis insertion.

    The class supports method chaining for fluent API usage and implements
    comparison operators based on string length.

    Example:
        >>> TODO = 'TODO'
    """

    def __init__(self, source: Any) -> None:
        """Initialize a SnipStr instance.

        Args:
            source: The source object to be wrapped. Will be converted to
                string when needed. The initial max length is set to the
                length of the string representation of source.
        """
        self._source = source

        self._max_lenght = len(str(source))
        self._side = 'right'
        self._w_ellipsis = False

    @property
    def source(self) -> Any:
        """Return the original source object.

        Returns:
            The source object that was passed to the constructor.
        """
        return self._source

    def snip_to(self, size: PositiveInt, /) -> SelfSnipStr:
        """Set the maximum length for string truncation.

        Args:
            size: The maximum length for the truncated string. Must be a
                positive integer.

        Returns:
            Self for method chaining.

        Raises:
            SnipSizeIsNotIntError: If size is not an integer.
            SnipSizeIsNotPositiveIntError: If size is zero or negative.
        """
        if not isinstance(size, int):
            raise SnipSizeIsNotIntError(size)
        if size <= 0:
            raise SnipSizeIsNotPositiveIntError(size)

        self._max_lenght = size

        return self

    def snip_side(self, side: SnipSide, /) -> SelfSnipStr:
        """Set the side from which to truncate the string.

        Args:
            side: The side to truncate from. Must be either 'left' or 'right'.
                - 'left': Truncate from the beginning of the string.
                - 'right': Truncate from the end of the string.

        Returns:
            Self for method chaining.

        Raises:
            SnipSideError: If side is not 'left' or 'right'.
        """
        if side not in ('left', 'right'):
            raise SnipSideError(side)

        self._side = side

        return self

    def with_ellipsis(self) -> SelfSnipStr:
        """Enable ellipsis insertion in the truncated string.

        When enabled, the ellipsis ('...') will be inserted at the truncation
        point. For 'right' side truncation, it replaces the last 3 characters.
        For 'left' side truncation, it replaces the first 3 characters.

        Returns:
            Self for method chaining.
        """
        self._w_ellipsis = True

        return self

    def _cut_back(self, current: str) -> str:
        """Truncate the string based on the configured side and max length.

        Args:
            current: The string to truncate.

        Returns:
            The truncated string.
        """
        if self._side == 'right':
            current = current[:self._max_lenght]
        elif self._side == 'left':
            current = current[self._max_lenght:]

        return current

    def _add_ellipsis(self, current: str) -> str:
        """Add ellipsis to the string if ellipsis mode is enabled.

        Args:
            current: The string to add ellipsis to.

        Returns:
            The string with ellipsis added if enabled, otherwise unchanged.
        """
        if self._w_ellipsis :
            elps = '...'

            if self._side == 'right':
                current = current[:-3] + elps
            elif self._side == 'left':
                current = elps + current[3:]

        return current

    def __len__(self) -> int:
        """Return the maximum length configured for truncation.

        Returns:
            The maximum length value.
        """
        return self._max_lenght

    def __str__(self) -> str:
        """Return the truncated string representation.

        Applies truncation and ellipsis based on the current configuration.

        Returns:
            The truncated string representation of the source object.
        """
        current = str(self._source)

        current = self._cut_back(current)
        current = self._add_ellipsis(current)

        return current

    def __hash__(self) -> int:
        """Return the hash value of the SnipStr instance.

        The hash is based on the source object, max length, side, and
        ellipsis settings.

        Returns:
            The hash value of the instance.
        """
        return hash(
            self._source,
            self._max_lenght,
            self._side,
            self._w_ellipsis,
        )

    def __eq__(self, other: SnipStrInstance | Any) -> bool:
        """Compare two SnipStr instances for equality.

        Two SnipStr instances are considered equal if they have the same
        source object, max length, side, and ellipsis settings.

        Args:
            other: Another object to compare with.

        Returns:
            True if both instances have the same configuration and source,
            False otherwise. Returns NotImplemented if other is not a
            SnipStr instance.
        """
        if not isinstance(other, SnipStr):
            return NotImplemented

        return all((
            (self._source == other._source),
            (self._max_lenght == other._max_lenght),
            (self._side == other._side),
            (self._w_ellipsis == other._w_ellipsis),
        ))

    def _total_tength(self):
        return self._max_lenght + (3 if self._w_ellipsis else 0)