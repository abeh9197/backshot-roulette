from ..entities import Dealer, DealerAction, GameConfig
from ..entities import PlayerAction
from ..entities import Turn

class Game:
    def __init__(self, config: GameConfig) -> None:
        self.__dealer: Dealer = config.dealer
        self.__player = config.player
        self.__shotgun = config.shotgun
        self.__round = 1
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
        """現在のターンがプレイヤーのターンかどうかを返す"""
        return self.turn.is_players

    def check_and_reload(self) -> str:
        """ショットガンのカートリッジがなくなった場合、リロードメッセージを返す"""
        if not self.__shotgun.has_ammo:
            self.__shotgun.reload()
            return "No more cartridges. Reloading the shotgun..."
        return ""

    def play_turn(self, player_action: PlayerAction = None) -> dict:
        """
        ターンをプレイして結果を返す。結果は辞書形式で、表示側が処理しやすいように構造化する。
        """
        result = {"message": "", "shot_fired": False, "target": None, "is_blank": False}

        if self.turn.is_dealers_turn:
            dealer_action = self.__generate_dealer_action()
            result.update(self.__apply_dealers_action(dealer_action))
        else:
            result.update(self.__apply_action(action=player_action))

        return result

    def switch_turn(self) -> None:
        self.turn.switch_turn()

    def __apply_action(self, action: PlayerAction) -> dict:
        target = self.__dealer if action.is_opponent else self.__player
        return self.__apply_shot(target=target)

    def __apply_dealers_action(self, action: DealerAction) -> dict:
        target = self.__player if action.is_player else self.__dealer
        return self.__apply_shot(target=target)

    def __apply_shot(self, target) -> dict:
        """
        ターゲットにショットを適用し、その結果を辞書形式で返す。
        :param target: ダメージを受ける対象（プレイヤーまたはディーラー）
        :return: 結果の辞書（shot_fired, target, is_blank, message）
        """
        cartridge = self.__shotgun.shoot()
        result = {
            "target": target.__class__.__name__,
            "shot_fired": True,
            "is_blank": cartridge.is_blank,
            "message": ""
        }

        if cartridge.is_blank:
            result["message"] = "空砲が発射されました。ターンが継続します。"
        else:
            target.take_damage()
            result["message"] = f"{target.__class__.__name__} にダメージが与えられました！"
            self.switch_turn()

        return result

    def __generate_dealer_action(self) -> DealerAction:
        return self.__dealer.decide_action()
