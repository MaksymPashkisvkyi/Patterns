from __future__ import annotations
from abc import ABC, abstractmethod


class FirstVersionGameInterface:
    """
        Абстракция устанавливает интерфейс для «управляющей» части двух иерархий
        классов. Она содержит ссылку на объект из иерархии Реализации и делегирует
        ему всю настоящую работу.
        """

    def __init__(self, game_engin: GameEngine) -> None:
        self._game_engin = game_engin

    def show(self) -> str:
        return (f"First Version of Game Interface:\n"
                f"{self._game_engin.start_game()}")


class SecondVersionGameInterface(FirstVersionGameInterface):
    def __init__(self, game_engin: GameEngine) -> None:
        super().__init__(game_engin)

    def show(self) -> str:
        return (f"Second Version of Game Interface:\n"
                f"{self._game_engin.start_game()}")


class GameEngine(ABC):
    """
        Реализация устанавливает интерфейс для всех классов реализации. Он не должен
        соответствовать интерфейсу Абстракции. На практике оба интерфейса могут быть
        совершенно разными. Как правило, интерфейс Реализации предоставляет только
        примитивные операции, в то время как Абстракция определяет операции более
        высокого уровня, основанные на этих примитивах.
    """

    @abstractmethod
    def start_game(self) -> str:
        pass


class UnrealEngine(GameEngine):
    def start_game(self) -> str:
        return 'Start with Unreal Engine'


class REDEngine(GameEngine):
    def start_game(self) -> str:
        return 'Start with RED Engine'


def client_code(game_interface: FirstVersionGameInterface) -> None:
    """
    За исключением этапа инициализации, когда объект Абстракции связывается с
    определённым объектом Реализации, клиентский код должен зависеть только от
    класса Абстракции. Таким образом, клиентский код может поддерживать любую
    комбинацию абстракции и реализации.
    """

    print(game_interface.show(), end="")


if __name__ == "__main__":
    """
    Клиентский код должен работать с любой предварительно сконфигурированной
    комбинацией абстракции и реализации.
    """

    engine = UnrealEngine()
    game = FirstVersionGameInterface(engine)
    client_code(game)

    print("\n")

    engine = REDEngine()
    game = SecondVersionGameInterface(engine)
    client_code(game)
