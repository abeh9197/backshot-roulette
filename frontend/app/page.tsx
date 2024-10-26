'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function Home() {
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  const startGame = async () => {
    try {
      const response = await fetch('/api/start-game', { method: 'POST' });
      if (!response.ok) {
        throw new Error('Failed to start game');
      }
      // ゲームが正常に開始されたらゲーム画面に遷移
      router.push('/game');
    } catch (error) {
      console.error('Error starting game:', error);
      setError('ゲームの開始に失敗しました。');
    }
  };

  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <h1 className="text-4xl font-bold mb-4">Backshot Roulette</h1>
      <button
        onClick={startGame}
        className="bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700 mb-4"
      >
        Start Game
      </button>
      {error && <p className="text-red-500">{error}</p>}
    </main>
  );
}
