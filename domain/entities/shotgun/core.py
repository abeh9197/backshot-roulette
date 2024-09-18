from .details import ShotgunDetails
from domain.entities import Cartridge, Cartridges


class Shotgun:
    def __init__(self, details: ShotgunDetails) -> None:
        self.__details = details
        self.__cartridges = self.__details.cartridges

    @property
    def cartridges(self) -> Cartridges:
        return self.__cartridges

    @property
    def has_ammo(self) -> bool:
        return not self.__cartridges.is_empty

    def reload(self) -> None:
        self.__cartridges = Cartridges(self.cartridges.capacity + 1)

    def shoot(self) -> Cartridge:
        return self.cartridges.discharge()
