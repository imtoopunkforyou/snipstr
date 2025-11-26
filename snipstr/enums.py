import enum


@enum.unique
class Sides(enum.Enum):
    LEFT = 'left'
    RIGHT = 'right'

    @classmethod
    def get_values(cls: type['Sides']) -> tuple[str, ...]:
        return tuple(side.value for side in cls)
