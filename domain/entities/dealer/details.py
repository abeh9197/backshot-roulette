class DealerDetails:
    def __init__(self, health: int = 3, intelligence: int = 1) -> None:
        self.__health = health
        self.__intelligence = intelligence

    @property
    def health(self) -> int:
        return self.__health

    @property
    def intelligence(self) -> int:
        return self.__intelligence
