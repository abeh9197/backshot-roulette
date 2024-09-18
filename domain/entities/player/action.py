from enum import Enum


class PlayerActionType(Enum):
    SELF = "自分に撃つ"
    OPPONENT = "相手に撃つ"

    @classmethod
    def choices(cls) -> list[str]:
        return [action.value for action in cls]


class PlayerAction:
    def __init__(self, target: str) -> None:
        self.__target = target

    @property
    def is_opponent(self) -> bool:
        return self.__target == PlayerActionType.OPPONENT

    @property
    def is_self(self) -> bool:
        return self.__target == PlayerActionType.SELF

    def __str__(self):
        return self.__target
