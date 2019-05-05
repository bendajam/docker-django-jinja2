from enum import Enum, unique


@unique
class DeclarativeEnum(Enum):
    def __new__(cls, value, description, *args):
        obj = object.__new__(cls)
        obj._value_ = int(value)
        obj.description = description
        for idx, val in enumerate(args):
            obj.__dict__[f'extra_{idx}'] = val
        return obj

    @classmethod
    def choices(cls):
        """Built in for helper in wtforms."""
        return [(choice.value, choice.description) for choice in cls]


# Example
class TOOLS(DeclarativeEnum):
    hammer = 1, "The Hammer"
    nail = 2, "Everythings a Nail"
