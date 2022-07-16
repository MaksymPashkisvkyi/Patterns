from abc import ABCMeta, abstractmethod


class ICommand(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute():
        pass


class Invoker:
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")


class Receiver:

    @staticmethod
    def open_command():
        print("Executing open command")

    @staticmethod
    def read_command():
        print("Executing read command")

    @staticmethod
    def close_command():
        print("Executing close command")


class Open(ICommand):

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.open_command()


class Read(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.read_command()


class Close(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.close_command()


if __name__ == '__main__':
    receiver = Receiver()

    # initialization command object
    open_file = Open(receiver)
    read_file = Read(receiver)
    close_file = Close(receiver)

    # register command in invoker
    invoker = Invoker()
    invoker.register("open", open_file)
    invoker.register("read", read_file)
    invoker.register("close", close_file)

    # run commands
    invoker.execute("open")
    invoker.execute("read")
    invoker.execute("close")
