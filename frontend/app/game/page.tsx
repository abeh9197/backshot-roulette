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
            <div className="flex space-x-2">
              {Array(gameState.player_health).fill(null).map((_, idx) => (
                <Image
                  key={idx}
                  src="/denryoku_mark.png"
                  alt="Player Health"
                  width={30}
                  height={30}
                />
              ))}
            </div>
          </div>
          <div className="mb-4">
            <h3 className="font-semibold">Dealer Health:</h3>
            <div className="flex space-x-2">
              {Array(gameState.dealer_health).fill(null).map((_, idx) => (
                <Image
                  key={idx}
                  src="/denryoku_mark.png"
                  alt="Dealer Health"
                  width={30}
                  height={30}
                />
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
