from abc import ABC, abstractmethod
from typing import Any

from typing_extensions import Self

from snipstr.constants import Sides
from snipstr.types import PositiveInt


class AbstractSnipStr(ABC):
    @abstractmethod
    def snip_to(self, size: PositiveInt) -> Self: ...

    @abstractmethod
    def by_side(self, side: Sides) -> Self: ...

    @abstractmethod
    def with_replacement_symbol(
        self,
        symbol: str | None = None,
        /,
    ) -> Self: ...

    @property
    @abstractmethod
    def source(self) -> Any: ...


class BaseSnipStr(AbstractSnipStr):
    def __init__(self, source: Any) -> None:
        self._source = source
        self._lenght = len(str(source))
        self._side = Sides.RIGHT.value
        self._replacement_symbol = ''

    @property
    def source(self) -> Any:
        return self._source

    def __repr__(self) -> str:
        source = (
            (self._source[:10] + '<...>' + self._source[-10:])
            if isinstance(self._source, str)
            else str(self._source)
        )
        msg = '{name}(source={source}, lenght={lenght}, side={side}, replacement_symbol={symbol})'

        return msg.format(
            source=source,
            name=self.__class__.__name__,
            lenght=self._lenght,
            side=self._side,
            symbol=(
                self._replacement_symbol
                if self._replacement_symbol
                else None,
            ),
        )


class ComparableSnipStr(BaseSnipStr):
    __slots__ = BaseSnipStr.__slots__

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return self._lenght < other._lenght

    def __le__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return self._lenght <= other._lenght

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return self._lenght > other._lenght

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return self._lenght >= other._lenght


class HashedSnipStr(BaseSnipStr):
    __slots__ = BaseSnipStr.__slots__

    def __hash__(self) -> int:
        attrs = tuple(getattr(self, attr) for attr in self.__slots__)

        return hash(attrs)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return all(
            getattr(self, attr) == getattr(other, attr)
            for attr in self.__slots__
        )


class BuilderSnipStr(BaseSnipStr):
    __slots__ = BaseSnipStr.__slots__

    def _build(self, current: str) -> str:
        current = str(current)
        current = self._cut_back(current)
        current = self._add_replacement_symbol(current)

        return current  # noqa: RET504

    def _cut_back(self, current: str) -> str:
        if self._side == Sides.RIGHT.value:
            current = current[: self._lenght]
        elif self._side == Sides.LEFT.value:
            current = current[self._lenght :]

        return current

    def _add_replacement_symbol(self, current: str) -> str:
        if self._replacement_symbol:
            symbol_lenght = len(self._replacement_symbol)
            if self._side == Sides.RIGHT.value:
                current = current[:-symbol_lenght] + self._replacement_symbol
            elif self._side == Sides.LEFT.value:
                current = self._replacement_symbol + current[symbol_lenght:]

        return current
