import json
from typing import Dict


class Iphone:

    def __init__(self, shared_state: list[str]) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"iPhone: Displaying shared ({s}) and unique ({u}) state.", end="")


class IphoneFactory:
    _iphone: Dict[str, Iphone] = {}

    def __init__(self, initial_flyweights: list[list[str]]) -> None:
        for state in initial_flyweights:
            self._iphone[self.get_key(state)] = Iphone(state)

    @staticmethod
    def get_key(state: list[str]) -> str:
        return "_".join(sorted(state))

    def get_iphone_info(self, shared_state: list[str]) -> Iphone:

        key = self.get_key(shared_state)

        if not self._iphone.get(key):
            print("iPhoneFactory: Can't find an iPhone version, creating new one.")
            self._iphone[key] = Iphone(shared_state)
        else:
            print("iPhoneFactory: Reusing existing iPhone version.")

        return self._iphone[key]

    def list_of_iphone(self) -> None:
        count = len(self._iphone)
        print(f"iPhoneFactory: I have {count} iPhones various:")
        print("\n".join(map(str, self._iphone.keys())), end="")


def add_iphone_to_mac_database(iphone: IphoneFactory, mac_address: str, name: str, version: str,
                               color: str) -> None:
    print("\n\nClient: Adding an iPhone to database.")
    flyweight = iphone.get_iphone_info([name, version, color])
    flyweight.operation(mac_address)


if __name__ == "__main__":
    iphone = IphoneFactory([
        ["IPhone", "4", "white"],
        ["IPhone", "4", "black"],
        ["IPhone", "4s", "white"],
        ["IPhone", "4s", "black"],
        ["IPhone", "5", "white"],
        ["IPhone", "5", "black"],
        ["IPhone", "5s", "white"],
        ["IPhone", "5s", "black"]
    ])

    iphone.list_of_iphone()

    add_iphone_to_mac_database(iphone, "88:AE:07:2F:79:A7", "IPhone", "5s", "black")

    add_iphone_to_mac_database(iphone, "88:AE:07:2F:81:T1", "IPhone", "6", "white ")

    print("\n")

    iphone.list_of_iphone()
