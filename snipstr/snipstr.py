from typing import Annotated, Any, TypeVar, final

from snipstr.base import ComparableByLength
from snipstr.constants import Sides
from snipstr.errors import (
    SnipSideError,
    SnipSizeIsNotIntError,
    SnipSizeIsNotPositiveIntError,
)

SelfSnipStr = TypeVar('SelfSnipStr', bound='SnipStr')
SnipStrInstance = TypeVar('SnipStrInstance', bound='SnipStr')

PositiveInt = Annotated[int, 'An integer that is greater than 0.']


@final
class SnipStr(ComparableByLength):
    """Example:
    >>> TODO = 'TODO'
    """

    def __init__(self, source: Any) -> None:
        self._source = source
        self._max_lenght = len(str(source))
        self._side = Sides.RIGHT.value
        self._replacement_symbol = ''

    @property
    def source(self) -> Any:
        return self._source

    def snip_to(self, size: PositiveInt, /) -> SelfSnipStr:
        if not isinstance(size, int):
            raise SnipSizeIsNotIntError(size)
        if size <= 0:
            raise SnipSizeIsNotPositiveIntError(size)

        self._max_lenght = size

        return self

    def by_side(self, side: Sides, /) -> SelfSnipStr:
        if side not in Sides:
            raise SnipSideError(side)

        self._side = side

        return self

    def with_replacement_symbol(
        self,
        symbol: str | None = None,
        /,
    ) -> SelfSnipStr:
        default = '...'
        symbol = default if symbol is None else str(symbol)

        self._replacement_symbol = symbol

        return self

    def __len__(self) -> int:
        return self._max_lenght

    def __str__(self) -> str:
        return self._build(str(self._source))
