from fastapi import APIRouter, Depends
from ..domain.entities import Game
from ..main import game

router = APIRouter()

@router.get("/status")
def get_game_status(game: Game = Depends(lambda: game)):
    status = {
        "turn": game.turn.current_turn,
        "player_health": game.player.health,
        "dealer_health": game.dealer.health,
        "cartridges": [("🟥" if c.is_live else "🟩") for c in game.shotgun.cartridges.get_all()],
    }
    return status

@router.get("/over")
def is_game_over(game: Game = Depends(lambda: game)):
    return {"is_over": game.is_over}
