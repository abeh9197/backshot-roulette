from ..cartridge import Cartridges


class ShotgunDetails:
    def __init__(self, cartridges: Cartridges) -> None:
        self.__cartridges = cartridges

    @property
    def cartridges(self) -> Cartridges:
        return self.__cartridges
