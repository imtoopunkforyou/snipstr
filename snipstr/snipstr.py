from typing import Annotated, Self, final, Any, ClassVar, TypeAlias, Literal

from annotated_types import Gt

SnipSide: TypeAlias = Literal['left', 'right']

@final
class SnipStr:

    def __init__(self, source: Any) -> None:
        self._source = source

        self._max_lenght = len(str(source))
        self._side = 'right'
        self._w_ellipsis = False

    @property
    def source(self) -> Any:
        return self._source

    def snip_to(self, value: Annotated[int, Gt(0)], /) -> 'SnipStr':
        if value <= 0:
            err = 'The maximum length must be a positive number. You have set {0}'
            raise ValueError(err.format(value))
        self._max_lenght = value

        return self

    def snip_side(self, value: SnipSide, /) -> 'SnipStr':
        if value not in ('left', 'right'):
            raise

        self._side = value

        return self

    def with_ellipsis(self, value: bool | None = None, /) -> 'SnipStr':
        if value is not None or not isinstance(value, bool):
            raise

        self._w_ellipsis = True if value is None else value

        return self

    def as_string(self) -> str:
        return str(self)

    def _cut_back(self, value: str) -> str:
        if self._side == 'right':
            value = value[:self._max_lenght]
        elif self._side == 'left':
            value = value[self._max_lenght:]

        return value

    def _add_ellipsis(self, value: str) -> str:
        if self._w_ellipsis:
            if self._side == 'right':
                value = value[:-3] + '...'
            elif self._side == 'left':
                value = '...' + value[3:]

        return value

    def __len__(self) -> int:
        return self._max_lenght

    def __str__(self) -> str:
        current = str(self._source)

        current = self._cut_back(current)
        current = self._add_ellipsis(current)

        return current  # noqa: RET504

    def __hash__(self) -> int:
        return hash(self._source, self._max_lenght, self._side, self._w_ellipsis)

    def __eq__(self, other: 'SnipStr') -> bool:
        if not isinstance(other, SnipStr):
            return NotImplemented

        return all((
            (self._source == other._source),
            (self._max_lenght == other._max_lenght),
            (self._side == other._side),
            (self._w_ellipsis == other._w_ellipsis),
        ))

    def _result_length(self) -> int:
        return self._max_lenght + (3 if self._w_ellipsis else 0)

    def __lt__(self, other: 'SnipStr') -> bool:
        if not isinstance(other, SnipStr):
            return NotImplemented
        return self._result_length() < other._result_length()

    def __le__(self, other: 'SnipStr') -> bool:
        if not isinstance(other, SnipStr):
            return NotImplemented
        return self._result_length() <= other._result_length()

    def __gt__(self, other: 'SnipStr') -> bool:
        if not isinstance(other, SnipStr):
            return NotImplemented
        return self._result_length() > other._result_length()

    def __ge__(self, other: 'SnipStr') -> bool:
        if not isinstance(other, SnipStr):
            return NotImplemented
        return self._result_length() >= other._result_length()