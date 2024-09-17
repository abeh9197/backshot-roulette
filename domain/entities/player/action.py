class PlayerAction:
    def __init__(self, target: str) -> None:
        self.__target = target

    @property
    def is_dealer(self) -> bool:
        return self.__target == "dealer"

    @property
    def is_self(self) -> bool:
        return self.__target == "self"

    def __str__(self):
        return "自分に撃つ" if self.is_self else "ディーラーに撃つ"
