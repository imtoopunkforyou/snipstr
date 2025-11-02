import enum


@enum.unique
class Sides(str, enum.Enum):
    LEFT = 'left'
    RIGHT = 'right'
