'use client';

import Button from "@/components/Button";

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-4xl font-bold mb-4">Backshot Roulette</h1>
      <Button label="Start Game" onClick={() => alert("Game Starting...")} />
    </main>
  );
}
