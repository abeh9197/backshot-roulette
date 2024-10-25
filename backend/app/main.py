import argparse
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
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
from utils import DisplayManager

app = FastAPI()

# ゲームの初期設定
display = DisplayManager()
player = Player(details=PlayerDetails(name="Player 1"))
dealer = Dealer(details=DealerDetails())
shotgun = Shotgun(details=ShotgunDetails(cartridges=Cartridges(capacity=6)))
game_config = GameConfig(player=player, dealer=dealer, shotgun=shotgun)
game = Game(config=game_config)

@app.get("/")
def read_root():
    """
    ゲームのステータスを表示（簡単なエンドポイント）。
    """
    return {"message": "Welcome to Backshot Roulette API"}

@app.get("/game/status")
def get_game_status():
    """
    ゲームの現在のステータス（プレイヤー、ディーラーのヘルス、カートリッジの状態など）を取得。
    """
    status = {
        "turn": game.turn.current_turn,
        "player_health": game.player.health,
        "dealer_health": game.dealer.health,
        "cartridges": [("🟥" if c.is_live else "🟩") for c in game.shotgun.cartridges.get_all()],
    }
    return status

@app.post("/game/play-turn")
def play_turn(action: str = None):
    """
    プレイヤーのアクションを受け取り、ターンを進行させるエンドポイント。
    `action` が指定されない場合はディーラーのターンとして進行。
    """
    if action:
        # プレイヤーのターン
        turn_result = game.play_turn(player_action=action)
    else:
        # ディーラーのターン
        turn_result = game.play_turn()

    # ショットガンのリロードチェック
    reload_message = game.check_and_reload()

    return {
        "turn_result": turn_result,
        "reload_message": reload_message if reload_message else "No reload needed",
    }

@app.get("/game/over")
def is_game_over():
    """
    ゲームが終了しているかどうかを確認するエンドポイント。
    """
    return {"is_over": game.is_over}
