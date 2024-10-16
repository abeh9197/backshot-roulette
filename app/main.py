import argparse
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from domain.entities import (
    Cartridges,
    Dealer,
    DealerDetails,
    GameConfig,
    Player,
    PlayerDetails,
    Shotgun,
    ShotgunDetails,
)
from domain.usecase.game import Game, GameConfig
from interface_adapters import InputManager
from utils.logger import logger
from utils import DisplayManager


def main() -> None:
    print("Game Start")
    display = DisplayManager()
    input_manager = InputManager()

    # args = parse_args()

    # プレイヤーとディーラー（またはプレイヤー2）を設定
    player = Player(details=PlayerDetails(name="args.player_name"))
    dealer = Dealer(details=DealerDetails())

    # ショットガンの設定
    shotgun = Shotgun(details=ShotgunDetails(cartridges=Cartridges(capacity=6)))

    # ゲーム設定の構築
    game_config = GameConfig(player=player, dealer=dealer, shotgun=shotgun)
    game = Game(config=game_config)

    while not game.is_over:
        print(game.turn.current_turn)

        # Display cartridges and health
        display.cartridges(game=game)
        display.health(game=game)

        # プレイヤーのターンかどうかを確認して行動を決定
        if game.is_player_turn:
            action = input_manager.get_player_action()
        else:
            action = None  # ディーラーのアクションはGame内部で生成される

        # ターンを進行し、結果を取得
        turn_result = game.play_turn(player_action=action)

        # 結果をDisplayManagerに渡して表示
        display.display_turn_result(result=turn_result)

        # ショットガンのリロードが必要かチェック
        reload_message = game.check_and_reload()
        if reload_message:
            display.display_message(reload_message)

    print("Game Over")


if __name__ == "__main__":
    main()
