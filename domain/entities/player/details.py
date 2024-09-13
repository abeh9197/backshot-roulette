class PlayerDetails:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__health = 3

    @property
    def name(self) -> str:
        return self.__name

    @property
    def health(self) -> int:
        return self.__health