from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):

    def __init__(self):
        self._discount = None

    @abstractmethod
    def attach(self, customer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, customer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

    @property
    def discount(self):
        return self._discount


class StoreMail(Subject):
    _discount: int = None

    _customers: List[Observer] = []

    def attach(self, customer: Observer) -> None:
        print("Store mail: Attached an customer.")
        self._customers.append(customer)

    def detach(self, customer: Observer) -> None:
        self._customers.remove(customer)

    def notify(self) -> None:
        print("Store mail: Notifying customers...")
        for customer in self._customers:
            customer.update(self)

    def some_business_logic(self) -> None:
        print("\nStore mail: I'm doing something important.")
        self._discount = randrange(1, 10)

        print(f"Store mail: We have new discounts on some products goods: {self._discount}%")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update(self, store_mail: Subject) -> None:
        pass


class CustomerA(Observer):
    def update(self, store_mail: Subject) -> None:
        if store_mail.discount < 3:
            print("Concrete Customer A: Reacted to the event")


class CustomerB(Observer):
    def update(self, store_mail: Subject) -> None:
        if store_mail.discount == 0 or store_mail.discount >= 2:
            print("Concrete Customer B: Reacted to the event")


if __name__ == "__main__":

    store_mail = StoreMail()

    customer_a = CustomerA()
    store_mail.attach(customer_a)

    customer_b = CustomerB()
    store_mail.attach(customer_b)

    store_mail.some_business_logic()
    store_mail.some_business_logic()

    store_mail.detach(customer_a)

    store_mail.some_business_logic()
