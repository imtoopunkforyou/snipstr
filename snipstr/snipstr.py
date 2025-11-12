import sys
from typing import final

from snipstr.base import (
    BuilderSnipStr,
    ComparableSnipStr,
    HashedSnipStr,
)
from snipstr.constants import Sides
from snipstr.errors import (
    SnipSideError,
    SnipSizeIsNotIntError,
    SnipSizeIsNotPositiveIntError,
)
from snipstr.types import PositiveInt

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


@final
class SnipStr(ComparableSnipStr, HashedSnipStr, BuilderSnipStr):
    """Example:
    >>> TODO = 'TODO'
    """

    __slots__ = (
        '_lenght',
        '_replacement_symbol',
        '_side',
        '_source',
    )

    def snip_to(self, size: PositiveInt, /) -> Self:
        if not isinstance(size, int):
            raise SnipSizeIsNotIntError(size)
        if size <= 0:
            raise SnipSizeIsNotPositiveIntError(size)

        self._lenght = size

        return self

    def by_side(self, side: Sides | str, /) -> Self:
        if isinstance(side, str) and side in Sides.get_values():
            self._side = side
        elif isinstance(side, Sides) and side in Sides:
            self._side = side.value
        else:
            raise SnipSideError(side)

        return self

    def with_replacement_symbol(
        self,
        symbol: str | None = None,
        /,
    ) -> Self:
        default = '...'
        symbol = default if symbol is None else str(symbol)

        self._replacement_symbol = symbol

        return self

    def __len__(self) -> int:
        return self._lenght

    def __str__(self) -> str:
        return self._build(str(self._source))
