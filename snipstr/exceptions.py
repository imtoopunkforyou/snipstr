from typing import Any


class IsNotStringError(TypeError):
    def __init__(self, source: Any, /) -> None:
        msg = (
            'The object must be a string. '
            'Transform your `{0}` object yourself.'
        )
        super().__init__(msg.format(source))

class LengthIsNotIntError(TypeError):
    def __init__(self, max_len: Any, /) -> None:
        msg = (
            'The maximum length must be an integer. '
            'You are trying to specify `{0}`'
        )
        super().__init__(msg.format(max_len))

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
