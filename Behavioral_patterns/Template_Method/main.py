from __future__ import annotations

from abc import ABC, abstractmethod


class ShopDelivery(ABC):

    def template_delivery(self, customer: Client) -> None:
        self.get_order(customer)
        self.get_payment(customer)
        self.send()

    @staticmethod
    def get_order(customer: Client) -> None:
        print(f"Shop take order on {customer.order} from client.")

    @staticmethod
    def get_payment(customer: Client) -> None:
        print(f"Shop take {customer.payment} from customer by {customer.pay_type}.")

    @abstractmethod
    def send(self) -> None:
        pass

    def hook(self) -> None:
        pass


class DeliveryNP(ShopDelivery):

    def send(self) -> None:
        print("Shop send order to Nova Poshta.")


class DeliveryUP(ShopDelivery):

    def send(self) -> None:
        print("Shop send order to UkrPoshta.")


class Client:
    def __init__(self, pay_type, payment, mail, order):
        self.pay_type = pay_type
        self.payment = payment
        self.mail = mail
        self.order = order


if __name__ == "__main__":
    client_NP = Client('card', 100, 'NP', 'Fridge')
    client_UP = Client('cash', 340, 'UP', 'Microwave')

    delivery_np = DeliveryNP()
    delivery_up = DeliveryUP()

    clients = [client_UP, client_NP]

    for client in clients:
        if client.mail == "NP":
            delivery_np.template_delivery(client)
        elif client.mail == "UP":
            delivery_up.template_delivery(client)
