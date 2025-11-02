from abc import ABC, abstractmethod
from typing import Any, TypeVar

from snipstr.constants import Sides
from snipstr.types import PositiveInt

SelfAbstractSnipStr = TypeVar('SelfAbstractSnipStr', bound='AbstractSnipStr')


class SlotsSnipStr:
    __slots__ = (
        '_lenght',
        '_replacement_symbol',
        '_side',
        '_source',
    )


class AbstractSnipStr(ABC):
    @abstractmethod
    def snip_to(self, size: PositiveInt) -> SelfAbstractSnipStr: ...

    @abstractmethod
    def by_side(self, side: Sides) -> SelfAbstractSnipStr: ...

    @abstractmethod
    def with_replacement_symbol(
        self,
        symbol: str | None = None,
        /,
    ) -> SelfAbstractSnipStr: ...

    @abstractmethod
    @property
    def source(self) -> Any: ...


class ComparableSnipStr:
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


class HashedSnipStr:
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


class BuilderSnipStr:
    def _build(self, current: str) -> str:
        current = str(current)
        current = self._cut_back(current)

        return self._add_replacement_symbol(current)

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
