from .entities.game_config import GameConfig


class Game:
    def __init__(self, config: GameConfig) -> None:
        self.__dealer = config.dealer
        self.__player = config.player
        self.__shotgun = config.shotgun
        self.__round = 1

    @property
    def dealer(self):  # -> Dealer:
        return self.__dealer
    
    @property
    def player(self):
    return self.__player

    @property
    def shotgun(self):
        return self.__shotgun

    @property
    def round(self) -> int:
        return self.__round
