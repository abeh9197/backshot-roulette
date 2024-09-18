class DisplayManager:
    def __init__(self) -> None:
        pass

    def cartridges(self, game) -> None:
        """
        カートリッジの状態をシンボルで表示する。
        空砲は🟩、実包は🟥で表示。
        """
        symbols = [
            "🟥" if c.is_live else "🟩" for c in game.shotgun.cartridges.get_all()
        ]
        print(f"[{''.join(symbols)}]")

    def health(self, game) -> None:
        """
        プレイヤーとディーラーのヘルスを表示する。
        """
        symbol = "⚡"  # TODO: 外から自由に定義できるようにしたい。
        print(f"Player: Health: [{symbol * game.player.health}]")
        print(f"Dealer: Health: [{symbol * game.dealer.health}]")
