from abc import ABC, abstractmethod


class DrinkMachine(ABC):

    @abstractmethod
    def make_drink(self):
        pass

    def get_order(self):
        drink = self.make_drink()
        order = f"{drink.get_drink()}"
        return order


class TeaMachine(DrinkMachine):

    def make_drink(self):
        return Tea()


class CoffeeMachine(DrinkMachine):

    def make_drink(self):
        return Coffee()


class Drink(ABC):

    @abstractmethod
    def get_drink(self):
        pass


class Coffee(Drink):

    def get_drink(self) -> str:
        return "Coffee drink"


class Tea(Drink):

    def get_drink(self) -> str:
        return "Tea drink"


class Client:

    @staticmethod
    def make_order(drink: DrinkMachine):
        print(f"Give me a {drink.get_order()}, please.")


if __name__ == '__main__':
    client = Client

    print("\nTea order")
    client.make_order(TeaMachine())

    print("\nCoffee order")
    client.make_order(CoffeeMachine())

