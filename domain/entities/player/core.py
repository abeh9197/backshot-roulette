from .action import PlayerAction
from .details import PlayerDetails
from domain.entities.shotgun import Shotgun


class Player:
    def __init__(self, details: PlayerDetails) -> None:
        self.__details = details

    @property
    def name(self) -> str:
        return self.__details.name

    @property
    def health(self) -> int:
        return self.__details.health

    def action(self, shotgun: Shotgun, selected_action: PlayerAction) -> None:
        if selected_action.is_dealer:
            return self.__shoot_at_dealer(shotgun=shotgun)
        else:
            return self.__shoot_at_self(shotgun=shotgun)

    def __shoot_at_dealer(self, shotgun: Shotgun):
        return shotgun.shoot()

    def __shoot_at_self(self, shotgun: Shotgun):
        return shotgun.shoot()
