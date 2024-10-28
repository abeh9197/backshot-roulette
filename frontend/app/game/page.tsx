'use client';

import { useState, useEffect } from 'react';
import Image from 'next/image';

export default function GamePage() {
  const [gameState, setGameState] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchGameState = async () => {
      try {
        const response = await fetch('/api/game/status');
        if (!response.ok) {
          throw new Error('Failed to fetch game state');
        }
        const data = await response.json();
        setGameState(data);
      } catch (error) {
        console.error('Error fetching game state:', error);
        setError('ゲームの状態を取得できませんでした。');
      }
    };

    fetchGameState();
  }, []);

  const handlePlayerAction = async (action: string) => {
    try {
      const response = await fetch('/api/game/play-turn', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action }),
      });
      if (!response.ok) {
        throw new Error('Failed to play turn');
      }
      const data = await response.json();
      setGameState(data);
    } catch (error) {
      console.error('Error playing turn:', error);
      setError('ターンの実行に失敗しました。');
    }
  };

  return (
    <main className="smoke-background flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-4xl font-bold mb-4 text-foreground">Backshot Roulette - Game</h1>
      {error && <p className="text-error">{error}</p>}
      {gameState ? (
        <div className="w-full max-w-md bg-[#2c2c54] rounded-lg shadow-md p-6 space-y-4">
          <h2 className="text-2xl font-bold text-foreground">Game Status</h2>
          <div>
            <h3 className="font-semibold text-lg text-foreground">Current Turn: {gameState.turn}</h3>
          </div>
          <div>
            <h3 className="font-semibold text-lg text-foreground">Player Health:</h3>
            <div className="flex space-x-2">
              {Array(gameState.player_health).fill(null).map((_, idx) => (
                <Image
                  key={idx}
                  src="/denryoku_mark.png"
                  alt="Player Health"
                  width={30}
                  height={30}
                  className="pulse-light"
                />
              ))}
            </div>
          </div>
          <div>
            <h3 className="font-semibold text-lg text-foreground">Dealer Health:</h3>
            <div className="flex space-x-2">
              {Array(gameState.dealer_health).fill(null).map((_, idx) => (
                <Image
                  key={idx}
                  src="/denryoku_mark.png"
                  alt="Dealer Health"
                  width={30}
                  height={30}
                  className="pulse-light"
                />
              ))}
            </div>
          </div>
          <div>
            <h3 className="font-semibold text-lg text-foreground">Cartridges:</h3>
            <div className="flex space-x-2">
              {gameState?.cartridges?.map((cartridge: string, idx: number) => (
                <span key={idx} className={`text-2xl ${cartridge === '🟥' ? 'text-red-500' : 'text-green-500'}`}>
                  {cartridge}
                </span>
              ))}
            </div>
          </div>
          <div className="flex space-x-4">
            <button
              onClick={() => handlePlayerAction('self')}
              className="bg-primary text-foreground py-2 px-4 rounded hover:bg-secondary"
            >
              自分に撃つ
            </button>
            <button
              onClick={() => handlePlayerAction('opponent')}
              className="bg-red-500 text-foreground py-2 px-4 rounded hover:bg-red-700"
            >
              ディーラーに撃つ
            </button>
          </div>
        </div>
      ) : (
        <p className="text-foreground">Loading...</p>
      )}
    </main>
  );
}
