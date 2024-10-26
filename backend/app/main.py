import os
import sys
from fastapi import FastAPI
from app.api import game, status

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

app = FastAPI()

# APIルーターの登録
app.include_router(game.router, prefix="/game")
app.include_router(status.router, prefix="/game")

# エントリーポイント
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
