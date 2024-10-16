import argparse
from argparse import Namespace
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


# TODO: あとで実装する。
# def parse_args() -> Namespace:
#     parser = argparse.ArgumentParser(description="Backshot Roulette")
#     parser.add_argument("--name", required=False)
#     return parser.parse_args()    


def main() -> None:
    print("Game Start")
    display = DisplayManager()
    input_manager = InputManager()

    # args = parse_args()

    # プレイヤーとディーラー（またはプレイヤー2）を設定
    player = Player(details=PlayerDetails(name="args.player_name"))
    dealer = Dealer(details=DealerDetails())

    # ショットガンの設定
    shotgun = Shotgun(details=ShotgunDetails(cartridges=Cartridges(capacity=2)))

    # ゲーム設定の構築
    game_config = GameConfig(player=player, dealer=dealer, shotgun=shotgun)
    game = Game(config=game_config)

    while not game.is_over:
        print(game.turn.current_turn)
        display.cartridges(game=game)  # TODO: まとめたい
        display.health(game=game)
        if game.is_player_turn:
            action = input_manager.get_player_action()
        else:
            action = None

        game.play_turn(player_action=action)

        game.check_and_reload()

    print("Game Over")


if __name__ == "__main__":
    main()
