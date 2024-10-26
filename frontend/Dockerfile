# Node.js 18 をベースにしたイメージを使用
FROM node:18-alpine

# 作業ディレクトリを作成
WORKDIR /app

# package.jsonとpackage-lock.jsonをコピー
COPY package.json package-lock.json ./

# 依存関係をインストール
RUN npm install

# Tailwind CSSの依存パッケージをインストール
RUN npm install -D tailwindcss postcss autoprefixer

# アプリケーションの全コードをコピー
COPY . .

# Tailwindの設定ファイルを生成
RUN npx tailwindcss init -p

# アプリケーションを起動
CMD ["npm", "run", "dev"]

# ポート3000を公開
EXPOSE 3000
