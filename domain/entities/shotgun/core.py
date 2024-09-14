from .details import ShotgunDetails


class Shotgun:
    def __init__(self, details: ShotgunDetails) -> None:
        self.__details = details
