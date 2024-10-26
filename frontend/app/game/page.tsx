'use client';

import { useState, useEffect } from 'react';

export default function GamePage() {
  const [gameState, setGameState] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchGameState = async () => {
      try {
        const response = await fetch('/api/start-game', { method: 'POST' });
        if (!response.ok) {
          throw new Error('Failed to start game');
        }
        const data = await response.json();
        setGameState(data);
      } catch (error) {
        console.error('Error starting game:', error);
        setError('ゲームの開始に失敗しました。');
      }
    };

    fetchGameState();
  }, []);

  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-4xl font-bold mb-4">Backshot Roulette - Game</h1>
      {error && <p className="text-red-500">{error}</p>}
      {gameState ? (
        <div className="w-full max-w-md bg-white rounded-lg shadow-md p-4">
          <h2 className="text-2xl font-bold mb-2">Game Status</h2>
          <div className="mb-4">
            <h3 className="font-semibold">Current Turn: {gameState.turn}</h3>
          </div>
          <div className="mb-4">
            <h3 className="font-semibold">Player Health:</h3>
            <div className="flex">
              {Array(gameState.player_health).fill('⚡').map((_, idx) => (
                <span key={idx} className="text-green-500 text-2xl">⚡</span>
              ))}
            </div>
          </div>
          <div className="mb-4">
            <h3 className="font-semibold">Dealer Health:</h3>
            <div className="flex">
              {Array(gameState.dealer_health).fill('⚡').map((_, idx) => (
                <span key={idx} className="text-red-500 text-2xl">⚡</span>
              ))}
            </div>
          </div>
          <div className="mb-4">
            <h3 className="font-semibold">Cartridges:</h3>
            <div className="flex space-x-1">
              {gameState?.cartridges?.map((cartridge: string, idx: number) => (
                <span key={idx} className="text-2xl">
                  {cartridge}
                </span>
              ))}
            </div>
          </div>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </main>
  );
}
