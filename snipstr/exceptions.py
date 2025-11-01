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


class LengthIsNotPositiveError(ValueError):
    def __init__(self, max_len: Any, /) -> None:
        msg = (
            'The maximum length must be an positive integer. '
            'You are trying to specify `{0}`'
        )
        super().__init__(msg.format(max_len))

class InvalidSnipArgumentError(ValueError):
    def __init__(self, value: Any, /) -> None:
        msg = (
            'You can only snip by arguments `left`, `right` or `center`. '
            'Argument {0} is not suitable.'
        )
        super().__init__(msg.format(value))
