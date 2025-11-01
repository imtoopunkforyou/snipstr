from abc import ABC, abstractmethod
from typing import TypeVar

_T = TypeVar('T', bound='ComparableByLength')

class ComparableByLength(ABC):

    @abstractmethod
    def _total_tength(self) -> int: ...

    def __lt__(self, other: _T) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._total_tength() < other._result_length()

    def __le__(self, other: _T) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._total_tength() <= other._result_length()

    def __gt__(self, other: _T) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._total_tength() > other._result_length()

    def __ge__(self, other: _T) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._total_tength() >= other._result_length()
