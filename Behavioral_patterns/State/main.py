from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    _state = None

    def __init__(self, state: State) -> None:
        print('Machine turned on.')
        self.change_state_to(state)

    def change_state_to(self, state: State):
        print(f"Change state to {type(state).__name__}.")
        self._state = state
        self._state.context = self

    def start_btn(self):
        self._state.start()

    def stop_btn(self):
        self._state.stop()


class State(ABC):

    def __init__(self):
        self._context = None

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass


class Ready(State):
    def start(self) -> None:
        print("Ready state handles start button request.")
        print("Ready state wants to change the state of the context.")
        self.context.change_state_to(Wash())

    def stop(self) -> None:
        print("Ready state don't handles start button request.")
        ...


class Wash(State):
    def start(self) -> None:
        print("Wash state don't handles start button request.")
        ...

    def stop(self) -> None:
        print("Wash state handles stop button request.")
        print("Wash state wants to change the state of the context.")
        self.context.change_state_to(Ready())


if __name__ == "__main__":
    machine = Context(Ready())
    machine.start_btn()

    print()

    machine.stop_btn()
