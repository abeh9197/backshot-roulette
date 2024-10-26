from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional

from ..domain.entities import Game, PlayerAction
from ..main import initialize_game, game

router = APIRouter()

class PlayTurnRequest(BaseModel):
    action: Optional[str] = None

@router.post("/start")
def start_game():
    game = initialize_game()
    return {
        "status": "success",
        "message": "Game started successfully",
        "turn": game.turn.current_turn,
        "player_health": game.player.health,
        "dealer_health": game.dealer.health,
    }

@router.post("/play-turn")
def play_turn(request: PlayTurnRequest, game: Game = Depends(lambda: game)):
    if game.is_over:
        raise HTTPException(status_code=400, detail="Game is already over.")

    try:
        if request.action:
            turn_result = game.play_turn(player_action=request.action)
        else:
            turn_result = game.play_turn()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    reload_message = game.check_and_reload()

    return {
        "turn_result": turn_result,
        "reload_message": reload_message if reload_message else "No reload needed",
    }
