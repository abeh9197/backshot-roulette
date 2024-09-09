from dataclasses import dataclass


@dataclass
class GameConfig(dataclass):
    player: str
    dealer: str
    shotgun: str