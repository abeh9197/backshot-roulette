from logging import getLogger, StreamHandler, DEBUG, Formatter

# カスタムフォーマッタークラス
class CustomFormatter(Formatter):
    # 色の設定（ANSIエスケープシーケンス）
    COLORS = {
        'DEBUG': '\033[94m',   # 青
        'INFO': '\033[92m',    # 緑
        'WARNING': '\033[93m', # 黄色
        'ERROR': '\033[91m',   # 赤
        'CRITICAL': '\033[95m' # マゼンタ
    }
    RESET = '\033[0m'

    def format(self, record):
        # ログレベルに応じたフォーマット設定
        log_fmt = f"{self.COLORS.get(record.levelname, self.RESET)}[%(levelname)s] %(message)s{self.RESET}"
        if record.levelno == DEBUG:
            log_fmt = f"{self.COLORS['DEBUG']}[DEBUG] %(message)s{self.RESET}"
        formatter = Formatter(log_fmt)
        return formatter.format(record)

# ロガーの設定
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
handler.setFormatter(CustomFormatter())  # カスタムフォーマッターを設定
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False
