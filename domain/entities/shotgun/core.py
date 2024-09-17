from .details import ShotgunDetails
from domain.entities import Cartridge, Cartridges


class Shotgun:
    def __init__(self, details: ShotgunDetails) -> None:
        self.__details = details

    @property
    def cartridges(self) -> Cartridges:
        return self.__details.cartridges

    def shoot(self) -> Cartridge:
        return self.cartridges[0]
