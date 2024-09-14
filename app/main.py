# import argparse
# from argparse import Namespace
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.entities.cartridge import Cartridges
from domain.entities.game_config import GameConfig
from domain.entities.player import Player, PlayerDetails
from domain.entities.shotgun import Shotgun, ShotgunDetails


# TODO: あとで実装する。
# def parse_args() -> Namespace:
#     parser = argparse.ArgumentParser(description="Backshot Roulette")

def main() -> None:
    game_config = GameConfig(
        player=Player(details=PlayerDetails(name="peko")),
        dealer="dealer",
        shotgun=Shotgun(details=ShotgunDetails(cartridges=Cartridges(nums=2))) # TODO: この数ってここで決めていいの？
    )

    print(game_config.player.name)


if __name__ == "__main__":
    main()