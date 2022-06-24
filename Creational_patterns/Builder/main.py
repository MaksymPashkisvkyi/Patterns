from abc import ABC, abstractmethod

from typing import Any


class Engineer(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def design_engine(self) -> None:
        pass

    @abstractmethod
    def design_cabin(self) -> None:
        pass

    @abstractmethod
    def design_control_system(self) -> None:
        pass


class Machine:

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Plane(Machine):
    pass


class Ship(Machine):
    pass


class Car(Machine):
    pass


class PlaneEngineer(Engineer):
    def __init__(self) -> None:
        self._product = None
        self.reset()

    def reset(self):
        self._product = Plane()

    @property
    def product(self) -> None:
        product = self._product
        self.reset()
        return product

    def design_engine(self) -> None:
        self._product.add('Plane Engine')

    def design_cabin(self) -> None:
        self._product.add('Plane Cabin')

    def design_control_system(self) -> None:
        self._product.add('Plane Control System')


class ShipEngineer(Engineer):
    def __init__(self) -> None:
        self._product = None
        self.reset()

    def reset(self):
        self._product = Ship()

    @property
    def product(self) -> None:
        product = self._product
        self.reset()
        return product

    def design_engine(self) -> None:
        self._product.add('Ship Engine')

    def design_cabin(self) -> None:
        self._product.add('Ship Cabin')

    def design_control_system(self) -> None:
        self._product.add('Ship Control System')


class CarEngineer(Engineer):
    def __init__(self) -> None:
        self._product = None
        self.reset()

    def reset(self):
        self._product = Car()

    @property
    def product(self) -> None:
        product = self._product
        self.reset()
        return product

    def design_engine(self) -> None:
        self._product.add('Car Engine')

    def design_cabin(self) -> None:
        self._product.add('Car Cabin')

    def design_control_system(self) -> None:
        self._product.add('Car Control System')


class Director:

    def __init__(self) -> None:
        self._engineer = None

    @property
    def engineer(self) -> Engineer:
        return self._engineer

    @engineer.setter
    def engineer(self, engineer: Engineer) -> None:
        self._engineer = engineer

    def build_full_featured_product(self) -> None:
        self.engineer.design_cabin()
        self.engineer.design_engine()
        self.engineer.design_control_system()


if __name__ == "__main__":
    director = Director()

    plane_engineer = PlaneEngineer()
    director.engineer = plane_engineer
    print("\n\nPlane full featured product: ")
    director.build_full_featured_product()
    plane_engineer.product.list_parts()

    ship_engineer = ShipEngineer()
    director.engineer = ship_engineer
    print("\n\nShip full featured product: ")
    director.build_full_featured_product()
    ship_engineer.product.list_parts()

    car_engineer = CarEngineer()
    director.engineer = car_engineer
    print("\n\nCar full featured product: ")
    director.build_full_featured_product()
    car_engineer.product.list_parts()

