import random


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

        # リストの順番を壊さないように、ランダムな順番でコピーを生成
        randomized_symbols = random.sample(symbols, len(symbols))
        print(f"[{''.join(randomized_symbols)}]")
        print(f"実包: {game.shotgun.cartridges.num_live}発 空砲: {game.shotgun.cartridges.num_blank}発")

    def health(self, game) -> None:
        """
        プレイヤーとディーラーのヘルスを表示する。
        """
        symbol = "⚡"  # TODO: 外から自由に定義できるようにしたい。
        print(f"Player: Health: [{symbol * game.player.health}]")
        print(f"Dealer: Health: [{symbol * game.dealer.health}]")

    def display_turn_result(self, result: dict) -> None:
        """
        ゲームから返されたターン結果を受け取って表示する。
        """
        if result["shot_fired"]:
            if result["is_blank"]:
                print(result["message"])
            else:
                print(result["message"])
                print(f"ターゲット: {result['target']}")

    def display_message(self, message: str) -> None:
        """
        ゲーム中の任意のメッセージを表示する。
        """
        print(message)
