from dataclasses import dataclass
from .shotgun import Shotgun
from .player import Player


@dataclass
class GameConfig:
    player: Player
    dealer: str
    shotgun: Shotgun
