from .action import PlayerAction
from .details import PlayerDetails
from domain.entities.shotgun import Shotgun


class Player:
    def __init__(self, details: PlayerDetails) -> None:
        self.__details = details
        self.__health = self.__details.health

    @property
    def name(self) -> str:
        return self.__details.name

    @property
    def health(self) -> int:
        return self.__health

    @property
    def is_dead(self) -> bool:
        return self.__health == 0

    def take_damage(self) -> None:
        self.__health -= 1
