from dataclasses import dataclass
from .player import Player

@dataclass
class GameConfig(dataclass):
    player: Player
    dealer: str
    shotgun: str