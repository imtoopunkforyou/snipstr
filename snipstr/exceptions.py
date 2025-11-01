from typing import Any


class SnipSizeIsNotIntError(TypeError):
    def __init__(self, size: Any, /) -> None:
        msg = (
            'You must specify int for snip size. '
            'Value of `{0}` is not suitable'
        )
        super().__init__(msg.format(size))

class SnipSizeIsNotPositiveIntError(ValueError):
    def __init__(self, size: Any, /) -> None:
        msg = (
            'You must specify positive number for snip size. '
            'Value of `{0}` is not suitable'
        )
        super().__init__(msg.format(size))


class SnipSideError(ValueError):
    def __init__(self, side: Any, /) -> None:
        msg = (
            'The side can only be the values of `left` or `right`. '
            'Value of `{0}` is not suitable'
        )
        super().__init__(msg.format(side))

