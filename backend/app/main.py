import os
import sys
from fastapi import FastAPI, Depends, HTTPException, Body
from pydantic import BaseModel
from typing import Optional

# sys.path 設定
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# インポート
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

# FastAPI アプリケーションの作成
app = FastAPI()

# ゲームの初期設定
display = DisplayManager()

# グローバル変数の初期化
game = None


def initialize_game() -> Game:
    global game
    player = Player(details=PlayerDetails(name="Player 1"))
    dealer = Dealer(details=DealerDetails())
    shotgun = Shotgun(details=ShotgunDetails(cartridges=Cartridges(capacity=6)))
    game_config = GameConfig(player=player, dealer=dealer, shotgun=shotgun)
    game = Game(config=game_config)
    return game


@app.get("/")
def read_root():
    """
    ゲームのステータスを表示（簡単なエンドポイント）。
    """
    return {"message": "Welcome to Backshot Roulette API"}


@app.post("/start")
def start_game():
    """
    ゲームを初期化して開始するエンドポイント。
    """
    game = initialize_game()
    return {
        "status": "success",
        "message": "Game started successfully",
        "turn": game.turn.current_turn,
        "player_health": game.player.health,
        "dealer_health": game.dealer.health,
    }


@app.get("/game/status")
def get_game_status(game: Game = Depends(lambda: game)):
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


class PlayTurnRequest(BaseModel):
    action: Optional[str] = None


@app.post("/game/play-turn")
def play_turn(request: PlayTurnRequest, game: Game = Depends(lambda: game)):
    """
    プレイヤーのアクションを受け取り、ターンを進行させるエンドポイント。
    `action` が指定されない場合はディーラーのターンとして進行。
    """
    if game.is_over:
        raise HTTPException(status_code=400, detail="Game is already over.")

    # ターンを進行
    try:
        if request.action:
            turn_result = game.play_turn(player_action=request.action)
        else:
            turn_result = game.play_turn()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # ショットガンのリロードチェック
    reload_message = game.check_and_reload()

    return {
        "turn_result": turn_result,
        "reload_message": reload_message if reload_message else "No reload needed",
    }


@app.get("/game/over")
def is_game_over(game: Game = Depends(lambda: game)):
    """
    ゲームが終了しているかどうかを確認するエンドポイント。
    """
    return {"is_over": game.is_over}


# アプリケーションのエントリーポイント
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
