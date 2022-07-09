from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        self._parent = parent

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def operation(self) -> str:
        pass


class Item(Component):

    def operation(self) -> str:
        return "Item"


class Box(Component):

    def __init__(self) -> None:
        self._children: List[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Box({'+'.join(results)})"


def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":

    ship_container = Box()

    box1 = Box()
    box1.add(Item())
    box1.add(Item())

    box2 = Box()
    box2.add(Item())

    ship_container.add(box1)
    ship_container.add(box2)
    ship_container.add(Item())

    print("Ship container:")
    client_code(ship_container)
