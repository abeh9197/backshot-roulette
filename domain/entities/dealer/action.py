from enum import Enum


class DealerActionType(Enum):
    DEALER = "ディーラーに撃つ"
    PLAYER = "プレーヤーに撃つ"

    @classmethod
    def choices(cls) -> list[str]:
        return [action.value for action in cls]


class DealerAction:
    def __init__(self, target: str) -> None:
        self.__target = target

    @property
    def is_dealer(self) -> bool:
        return self.__target == DealerActionType.DEALER

    @property
    def is_player(self) -> bool:
        return self.__target == DealerActionType.PLAYER

    def __str__(self):
        return self.__target
