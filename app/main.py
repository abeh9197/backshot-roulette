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
from utils.logger import logger


# TODO: あとで実装する。
# def parse_args() -> Namespace:
#     parser = argparse.ArgumentParser(description="Backshot Roulette")


def main() -> None:
    game_config = GameConfig(
        player=Player(details=PlayerDetails(name="peko")),
        dealer=Dealer(details=DealerDetails()),
        shotgun=Shotgun(
            details=ShotgunDetails(cartridges=Cartridges(nums=2))
        ),  # TODO: この数ってここで決めていいの？
    )
    game = Game(config=game_config)

    while True:
        logger.debug("Game Round: %s", game.round)
        logger.info("Player: %s, Health: %s", game.player.name, game.player.health)
        break

if __name__ == "__main__":
    main()
