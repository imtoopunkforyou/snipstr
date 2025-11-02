from typing import Annotated, Any, Literal, TypeAlias, TypeVar, final

from snipstr.comparison import ComparableByLength
from snipstr.errors import (
    SnipSideError,
    SnipSizeIsNotIntError,
    SnipSizeIsNotPositiveIntError,
)

SnipSide: TypeAlias = Literal['left', 'right']

SelfSnipStr = TypeVar('SelfSnipStr', bound='SnipStr')
SnipStrInstance = TypeVar('SnipStrInstance', bound='SnipStr')

PositiveInt = Annotated[int, 'A positive integer.']

@final
class SnipStr(ComparableByLength):
    """Example:
    >>> TODO = 'TODO'
    """

    def __init__(self, source: Any) -> None:

        self._source = source

        self._max_lenght = len(str(source))
        self._side = 'right'
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

    def by_side(self, side: SnipSide, /) -> SelfSnipStr:
        if side not in ('left', 'right'):
            raise SnipSideError(side)

        self._side = side

        return self

    def with_replacement_symbol(
        self,
        symbol: str | None = None,
        /,
    ) -> SelfSnipStr:
        symbol = '...' if symbol is None else str(symbol)
        self._replacement_symbol = symbol

        return self

    def _cut_back(self, current: str) -> str:
        if self._side == 'right':
            current = current[:self._max_lenght]
        elif self._side == 'left':
            current = current[self._max_lenght:]

        return current

    def _add_replacement_symbol(self, current: str) -> str:
        if self._replacement_symbol:
            symbol_lenght = len(self._replacement_symbol)
            if self._side == 'right':
                current = current[:-symbol_lenght] + self._replacement_symbol
            elif self._side == 'left':
                current = self._replacement_symbol + current[symbol_lenght:]

        return current

    def __len__(self) -> int:
        return self._max_lenght

    def __str__(self) -> str:
        current = str(self._source)

        current = self._cut_back(current)
        current = self._add_ellipsis(current)

        return current

    def __hash__(self) -> int:
        return hash(
            self._source,
            self._max_lenght,
            self._side,
            self._replacement_symbol,
        )

    def __eq__(self, other: SnipStrInstance | Any) -> bool:
        if not isinstance(other, SnipStr):
            return NotImplemented

        return all((
            (self._source == other._source),
            (self._max_lenght == other._max_lenght),
            (self._side == other._side),
            (self._replacement_symbol == other._replacement_symbol),
        ))

    def _total_tength(self) -> int:
        return self._max_lenght + len(self._replacement_symbol)
