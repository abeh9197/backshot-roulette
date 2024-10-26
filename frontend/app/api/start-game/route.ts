import { NextResponse } from 'next/server';

export async function POST() {
  try {
    // Docker コンテナ内のネットワークを使用してバックエンドにアクセス
    const response = await fetch('http://backend:8000/start', {
      method: 'POST',
    });

    if (!response.ok) {
      throw new Error('Failed to fetch from backend');
    }

    const data = await response.json();

    return NextResponse.json(data);
  } catch (error) {
    console.error('Error in /api/start-game:', error);
    return NextResponse.json({ error: 'Internal Server Error' }, { status: 500 });
  }
}
