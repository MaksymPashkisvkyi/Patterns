class CentralBankMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class CentralBank(metaclass=CentralBankMeta):
    def some_business_logic(self):
        pass


if __name__ == "__main__":

    s1 = CentralBank()
    s2 = CentralBank()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
