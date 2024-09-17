# import argparse
# from argparse import Namespace
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


def main() -> None:
    logger.info("Game Start")
    display = DisplayManager()
    input_manager = InputManager()

    while True:
        player = Player(details=PlayerDetails(name="peko"))  # TODO: まとめたい
        dealer = Dealer(details=DealerDetails())
        shotgun = Shotgun(
            details=ShotgunDetails(
                cartridges=Cartridges(nums=2)
            )  # TODO: この数ってここで決めていいの？
        )
        game_config = GameConfig(
            player=player,
            dealer=dealer,
            shotgun=shotgun,
        )
        game = Game(config=game_config)
        display.cartridges(game=game)  # TODO: まとめたい
        display.health(game=game)
        ret = input_manager.get_player_action()
        print(ret)
        break


if __name__ == "__main__":
    main()
