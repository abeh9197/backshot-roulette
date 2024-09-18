import readchar
from domain.entities.player.action import PlayerAction, PlayerActionType


class InputManager:
    def __init__(self) -> None:
        pass

    def get_player_name(self) -> str:
        return input("Input players name: ") or "Anonymous"

    def get_player_action(self) -> PlayerAction:
        """
        プレイヤーに矢印キーまたはWASDで自分に撃つか、ディーラーに撃つかを選ばせる。
        :return: 'self' (自分に撃つ) または 'dealer' (ディーラーに撃つ)
        """
        selected_index = 0

        print(
            "\033[31m矢印キー(↑↓)またはWASDキー(W/S)で選択し、Enterで決定してください。\033[0m"
        )
        options = PlayerActionType.choices()
        while True:
            for i, option in enumerate(options):
                if i == selected_index:
                    print(f"> {option}")
                else:
                    print(f"  {option}")

            key = readchar.readkey()

            if key in ["s", "\x1b[B"]:
                selected_index = min((selected_index + 1, len(options) - 1))
            elif key in ["w", "\x1b[A"]:
                selected_index = max(selected_index - 1, 0)
            elif key in ["\r", "\n"]:
                return PlayerAction("self" if selected_index == 0 else "dealer")

            # 選択肢の表示をクリア（コンソール上でリフレッシュ）
            print("\033c", end="")
            # 再表示
            print(
                "\033[31m矢印キー(↑↓)またはWASDキー(W/S)で選択し、Enterで決定してください。\033[0m"
            )
