from enum import Enum
from domain.entities.dealer import Dealer
from domain.entities.player import Player


class TurnType(Enum):
    DEALER = 0
    FIRST_PLAYER = 1
    SECOND_PLAYER = 2


class Turn:
    def __init__(self, player, opponent) -> None:
        self.__player = player
        self.__opponent = opponent
        self.__current_turn = TurnType.FIRST_PLAYER  # 初期状態はプレイヤー1のターン

    @property
    def current_turn(self) -> TurnType:
        return self.__current_turn

    def switch_turn(self) -> None:
        if self.is_first_players_turn:
            if isinstance(self.__opponent, Dealer):
                self.__current_turn = TurnType.DEALER
            else:
                self.__current_turn = TurnType.SECOND_PLAYER
        else:
            self.__current_turn = TurnType.FIRST_PLAYER

    @property
    def is_dealers_turn(self) -> bool:
        return self.__current_turn == TurnType.DEALER

    @property
    def is_first_players_turn(self) -> bool:
        return self.__current_turn == TurnType.FIRST_PLAYER

    @property
    def is_second_players_turn(self) -> bool:
        return self.__current_turn == TurnType.SECOND_PLAYER

    @property
    def is_dealers(self) -> bool:
        return self.is_dealers_turn

    @property
    def is_players(self) -> bool:
        return self.is_first_players_turn or self.is_second_players_turn
