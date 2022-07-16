from __future__ import annotations

from abc import ABC


class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass


class Manager(Mediator):
    def __init__(self, worker: Worker, client: Client) -> None:
        self._worker = worker
        self._worker.manager = self
        self._client = client
        self._client.manager = self

    def notify(self, sender: object, event: str) -> None:
        if event == "order_project":
            print("Manager reacts on an order and triggers following operations:")
            self._worker.work()
        elif event == "get_pay":
            print("Manager reacts on payment and triggers following operations:")
            self._client.pay()


class BaseComponent:
    def __init__(self, manager: Manager = None) -> None:
        self._manager = manager

    @property
    def manager(self) -> Manager:
        return self._manager

    @manager.setter
    def manager(self, manager: Manager) -> None:
        self._manager = manager


class Worker(BaseComponent):
    def work(self) -> None:
        print("Worker works.")
        self.manager.notify(self, "work")

    def get_pay(self) -> None:
        print("Worker say to manager about payment.")
        self.manager.notify(self, "get_pay")
        print("Worker get payment.")


class Client(BaseComponent):
    def order_project(self) -> None:
        print("The client orders the project from the manager.")
        self.manager.notify(self, "order_project")

    def pay(self) -> None:
        print("The client pays for the project.")
        self.manager.notify(self, "pay")


if __name__ == "__main__":
    worker = Worker()
    client = Client()
    manager = Manager(worker, client)

    print("Client order the project.")
    client.order_project()
    print("\n", end="")

    print("Worker want payment.")
    worker.get_pay()
