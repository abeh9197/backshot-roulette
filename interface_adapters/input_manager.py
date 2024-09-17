import keyboard


class InputManager:
    def __init__(self) -> None:
        pass

    def get_player_name(self) -> str:
        return input("Input players name: ") or "Anonymous"

    def get_player_action(self) -> str:
        """
        プレイヤーに矢印キーまたはWASDで自分に撃つか、ディーラーに撃つかを選ばせる。
        :return: 'self' (自分に撃つ) または 'dealer' (ディーラーに撃つ)
        """
        options = ["自分に撃つ", "ディーラーに撃つ"]
        selected_index = 0

        print(
            "\033[31m矢印キー(↑↓)またはWASDキー(W/S)で選択し、Enterで決定してください。\033[0m"
        )

        while True:
            for i, option in enumerate(options):
                if i == selected_index:
                    print(f"> {option}")
                else:
                    print(f"  {option}")

            key = keyboard.read_event()

            if key.event_type == keyboard.KEY_DOWN:
                if key.name in ["down", "s"]:
                    selected_index = min((selected_index + 1, len(options) - 1))
                elif key.name in ["up", "w"]:
                    selected_index = max(selected_index - 1, 0)
                # 確定
                elif key.name == "enter":
                    if selected_index == 0:
                        return "self"
                    elif selected_index == 1:
                        return "dealer"

            # 選択肢の表示をクリア（コンソール上でリフレッシュ）
            print("\033c", end="")
            # 再表示
            print(
                "\033[31m矢印キー(↑↓)またはWASDキー(W/S)で選択し、Enterで決定してください。\033[0m"
            )
