from ..entities import Dealer, DealerAction, GameConfig
from ..entities import PlayerAction
from ..entities import Turn


class Game:
    def __init__(self, config: GameConfig) -> None:
        self.__dealer: Dealer = config.dealer
        self.__player = config.player
        self.__shotgun = config.shotgun
        self.__round = 1
        self.__is_switch_turn = False
        self.turn = Turn(player=self.__player, opponent=self.__dealer)

    @property
    def dealer(self):
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

    @property
    def is_over(self) -> bool:
        return self.player.is_dead or self.dealer.is_dead

    @property
    def is_player_turn(self) -> bool:
        return self.turn.is_players

    def check_and_reload(self) -> None:
        if not self.__shotgun.has_ammo:
            print("No more cartridges. Reloading the shotgun...")
            self.__shotgun.reload()

    def play_turn(self, player_action: PlayerAction = None) -> None:
        if self.turn.is_dealers_turn:
            self.__generate_dealer_action()
        else:
            self.__apply_action(action=player_action)

    def switch_turn(self) -> None:
        self.turn.switch_turn()

    def __apply_action(self, action: PlayerAction) -> None:
        if action.is_opponent:
            print()
            self.__apply_shot(target=self.__dealer)
        else:
            self.__apply_shot(target=self.__player)

    def __apply_dealers_action(self, action: DealerAction) -> None:
        if action.is_dealer:
            self.__apply_shot(target=self.__dealer)
        else:
            self.__apply_shot(target=self.__player)

    def __apply_shot(self, target) -> None:
        """
        指定されたターゲット（プレイヤーまたはディーラー）に対してショットを適用する。
        :param target: ダメージを受ける対象（プレイヤーまたはディーラー）
        """
        cartridge = self.__shotgun.shoot()
        if cartridge.is_blank:
            # 空砲の場合の処理（必要であればここに追加）
            print("空砲が発射されました。")
        else:
            # 実包の場合は対象にダメージを与える
            target.take_damage()
            print(f"{target.__class__.__name__} にダメージが与えられました！")
            self.switch_turn()

    def __generate_dealer_action(self) -> DealerAction:
        self.__apply_dealers_action(self.__dealer.decide_action())
