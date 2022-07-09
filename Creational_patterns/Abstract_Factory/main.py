from abc import ABC, abstractmethod


class Coffee(ABC):

    @abstractmethod
    def get_coffee(self) -> str:
        pass


class Espresso(Coffee):

    def get_coffee(self) -> str:
        return "espresso"


class Americano(Coffee):

    def get_coffee(self) -> str:
        return "americano"


class Tea(ABC):

    @abstractmethod
    def get_tea(self) -> str:
        pass


class GreenTea(Tea):

    def get_tea(self) -> str:
        return "green tea"


class BlackTea(Tea):

    def get_tea(self) -> str:
        return "black tea"


class DrinkMachine(ABC):

    @abstractmethod
    def make_coffee(self) -> Coffee:
        pass

    @abstractmethod
    def make_tea(self) -> Tea:
        pass


class FirstDrinkMachine(DrinkMachine):
    """
    Первая машинка умеет готовить черный чай и эспессо
    """

    def make_tea(self) -> Tea:
        return BlackTea()

    def make_coffee(self) -> Coffee:
        return Espresso()


class SecondDrinkMachine(DrinkMachine):
    """
    Вторая машинка умеет готовить залёный чай и американо
    """

    def make_tea(self) -> Tea:
        return GreenTea()

    def make_coffee(self) -> Coffee:
        return Americano()


class Client:

    @staticmethod
    def make_order(machine: DrinkMachine) -> None:

        coffee = machine.make_coffee()
        tea = machine.make_tea()

        print(coffee.get_coffee())
        print(tea.get_tea())


if __name__ == '__main__':
    client = Client()

    print("\nClient use first drink machine")
    client.make_order(FirstDrinkMachine())

    print("\nClient use second drink machine")
    client.make_order(SecondDrinkMachine())
