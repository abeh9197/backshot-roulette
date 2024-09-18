from ..entities import GameConfig
from ..entities import PlayerAction


class Game:
    def __init__(self, config: GameConfig) -> None:
        self.__dealer = config.dealer
        self.__player = config.player
        self.__shotgun = config.shotgun
        self.__round = 1

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

    def play_turn(self, player_action: PlayerAction) -> None:
        if player_action.is_opponent:
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
