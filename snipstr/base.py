import sys
from abc import ABC, abstractmethod

from snipstr.constants import Sides
from snipstr.types import PositiveInt

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self


class AbstractSnipStr(ABC):
    @abstractmethod
    def snip_to(self, size: PositiveInt, /) -> Self: ...

    @abstractmethod
    def by_side(self, side: Sides | str, /) -> Self: ...

    @abstractmethod
    def with_replacement_symbol(
        self,
        symbol: str | None = None,
        /,
    ) -> Self: ...

    @property
    @abstractmethod
    def source(self) -> object: ...


class BaseSnipStr(AbstractSnipStr):
    def __init__(self, source: object) -> None:
        self._source = source
        self._lenght = len(str(source))
        self._side = Sides.RIGHT.value
        self._replacement_symbol = ''

    @property
    def source(self) -> object:
        return self._source

    def __repr__(self) -> str:
        maximum_text_length = 30
        if (
            isinstance(self._source, str)
            and len(self._source) > maximum_text_length
        ):
            beginning_of_source = self._source[:10]
            end_of_source = self._source[-10:]
            source = '{} <...> {}'.format(beginning_of_source, end_of_source)
        else:
            source = str(self._source)

        msg = (
            '{name}(source={source}, '
            'length={length}, '
            'side={side}, '
            'replacement_symbol={symbol})'
        )

        return msg.format(
            source=source,
            name=self.__class__.__name__,
            length=self._lenght,
            side=self._side,
            symbol=(
                self._replacement_symbol if self._replacement_symbol else None,
            ),
        )


class ComparableSnipStr(BaseSnipStr):
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
    def __hash__(self) -> int:
        attrs = tuple(  # type: ignore[var-annotated]
            getattr(self, attr) for attr in self.__slots__
        )

        return hash(attrs)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented

        return all(  # type: ignore[var-annotated]
            getattr(self, attr) == getattr(other, attr)
            for attr in self.__slots__
        )


class BuilderSnipStr(BaseSnipStr):
    def _build(self, current: str) -> str:
        current = str(current)
        current = self._cut_back(current)
        current = self._add_replacement_symbol(current)

        return current  # noqa: RET504

    def _cut_back(self, current: str) -> str:
        if self._side == Sides.RIGHT.value:
            current = current[: self._lenght]
        elif self._side == Sides.LEFT.value:
            current = current[-self._lenght :]

        return current

    def _add_replacement_symbol(self, current: str) -> str:
        if self._replacement_symbol:
            symbol_lenght = len(self._replacement_symbol)
            if self._side == Sides.RIGHT.value:
                current = current[:-symbol_lenght] + self._replacement_symbol
            elif self._side == Sides.LEFT.value:
                current = self._replacement_symbol + current[symbol_lenght:]

        return current
