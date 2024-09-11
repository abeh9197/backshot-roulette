import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from domain.entities.player import Player, PlayerDetails
from domain.entities.game_config import GameConfig


def main() -> None:
    game_config = GameConfig(
        player=Player(details=PlayerDetails(name="peko")),
        dealer="dealer",
        shotgun="shotgun"
    )

    print(game_config.player.name)


if __name__ == "__main__":
    main()