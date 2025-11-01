from abc import ABC, abstractmethod
from typing import TypeVar

_T = TypeVar('_T', bound='ComparableByLength')

class ComparableByLength(ABC):
    """Abstract base class for objects that can be compared by length.

    This class provides comparison operators (<, <=, >, >=) based on the
    total length of objects. Subclasses must implement the `_total_tength`
    method to define how the length is calculated.

    The comparison is performed using the abstract `_total_tength` method
    which must be implemented by subclasses.
    """

    @abstractmethod
    def _total_tength(self) -> int:
        """Calculate the total length of the object.

        This method must be implemented by subclasses to define how
        the length should be calculated for comparison purposes.

        Returns:
            The total length of the object as an integer.
        """

    def __lt__(self, other: _T) -> bool:
        """Compare if this object is less than another by length.

        Args:
            other: Another object of the same type to compare with.

        Returns:
            True if this object's length is less than the other's length,
            False otherwise. Returns NotImplemented if other is not an
            instance of the same type.
        """
        if not isinstance(other, type(self)):
            return NotImplemented
        return self._total_tength() < other._result_length()

    def __le__(self, other: _T) -> bool:
        """Compare if this object is less than or equal to another by length.

        Args:
            other: Another object of the same type to compare with.

        Returns:
            True if this object's length is less than or equal to the other's
            length, False otherwise. Returns NotImplemented if other is not an
            instance of the same type.
        """
        if not isinstance(other, type(self)):
            return NotImplemented

        return self._total_tength() <= other._result_length()

    def __gt__(self, other: _T) -> bool:
        """Compare if this object is greater than another by length.

        Args:
            other: Another object of the same type to compare with.

        Returns:
            True if this object's length is greater than the other's length,
            False otherwise. Returns NotImplemented if other is not an
            instance of the same type.
        """
        if not isinstance(other, type(self)):
            return NotImplemented

        return self._total_tength() > other._result_length()

    def __ge__(self, other: _T) -> bool:
        """Compare if this object is greater than or equal to another by length.

        Args:
            other: Another object of the same type to compare with.

        Returns:
            True if this object's length is greater than or equal to the other's
            length, False otherwise. Returns NotImplemented if other is not an
            instance of the same type.
        """
        if not isinstance(other, type(self)):
            return NotImplemented

        return self._total_tength() >= other._result_length()
