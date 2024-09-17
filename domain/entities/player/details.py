class PlayerDetails:
    def __init__(self, name: str, health: int = 3) -> None:
        self.__name = name
        self.__health = health

    @property
    def name(self) -> str:
        return self.__name

    @property
    def health(self) -> int:
        return self.__health