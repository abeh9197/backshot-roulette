from .details import PlayerDetails


class Player:
    def __init__(self, details: PlayerDetails) -> None:
        self.__details = details

    @property
    def name(self) -> str:
        return self.__details.name

    @property
    def health(self) -> int:
        return self.__details.health
