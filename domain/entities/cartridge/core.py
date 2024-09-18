from enum import Enum
import random
from utils.logger import logger


class CartridgeType(Enum):
    """
    空砲: blank
    実包: live
    """

    BLANK = 0
    LIVE = 1


class Cartridge:
    def __init__(self, cartridge_type: CartridgeType = CartridgeType.BLANK) -> None:
        self.__type = cartridge_type

    def __str__(self):
        return "実包" if self.is_live else "空砲"

    @property
    def is_live(self) -> bool:
        return self.__type == CartridgeType.LIVE

    @property
    def is_blank(self) -> bool:
        return self.__type == CartridgeType.BLANK


class Cartridges:
    def __init__(self, capacity: int) -> None:
        self.__cartridges = self.__load_cartridges(capacity=capacity)
        self.__capacity = capacity

    def __len__(self) -> int:
        return len(self.__cartridges)

    def __iter__(self):
        return iter(self.__cartridges)

    def __getitem__(self, index):
        return self.__cartridges[index]

    def __str__(self):
        return "".join("🟥" if c.is_live else "🟩" for c in self.__cartridges)

    def __load_cartridges(self, capacity: int) -> list[Cartridge]:
        cartridges = [
            Cartridge(random.choice(list(CartridgeType))) for _ in range(capacity)
        ]
        cartridge_types = ["実包" if c.is_live else "空砲" for c in cartridges]
        logger.info(f"{capacity} cartridges loaded: {', '.join(cartridge_types)}")
        return cartridges

    @property
    def is_empty(self) -> bool:
        return len(self.__cartridges) == 0

    @property
    def capacity(self) -> int:
        return self.__capacity

    def get_all(self) -> list[Cartridge]:
        return self.__cartridges

    def discharge(self, index: int = -1) -> Cartridge:
        if not self.__cartridges:
            raise IndexError("カートリッジがありません。")

        return self.__cartridges.pop(index)
