# ベースイメージを指定（Python 3.9）
FROM python:3.9-slim

# 作業ディレクトリを作成
WORKDIR /app

# ホストマシンからコンテナへ requirements.txt をコピー
COPY requirements.txt /app/

# 依存パッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをすべてコピー
COPY . /app/

# アプリケーションの起動コマンドを設定 (FastAPI の場合)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# ポート8000を公開
EXPOSE 8000
