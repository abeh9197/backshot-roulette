import { NextResponse } from 'next/server';

export async function GET() {
  try {
    // Dockerコンテナ内のネットワークを使用してバックエンドのゲームステータスにアクセス
    const response = await fetch('http://backend:8000/game/status', {
      method: 'GET',
    });

    if (!response.ok) {
      throw new Error('Failed to fetch game status from backend');
    }

    const data = await response.json();
    return NextResponse.json(data);
  } catch (error) {
    console.error('Error in /api/game/status:', error);
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
