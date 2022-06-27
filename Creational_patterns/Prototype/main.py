import copy


class IPhone:

    def __init__(self, name, details):
        self.name = name
        self.details = details

    def __copy__(self):
        # First, let's create copies of the nested objects.
        details = copy.copy(self.details)
        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(
            self.name, details
        )
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memo=None):
        if memo is None:
            memo = {}

        # First, let's create copies of the nested objects.
        details = copy.deepcopy(self.details, memo)

        # Then, let's clone the object itself, using the prepared clones of the
        # nested objects.
        new = self.__class__(
            self.name, details
        )
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new


if __name__ == "__main__":
    name = 'IPhone 4 16 GB'
    details = {
        'battery capacity': name,
        'memory': '16 GB',
        'other_details': 'other_details'
    }

    iPhone_4_16_GB = IPhone(name, details)

    iPhone_4_32_GB = copy.deepcopy(iPhone_4_16_GB)
    iPhone_4_32_GB.name = 'iPhone 4 32 GB'
    iPhone_4_32_GB.details['memory'] = '32 GB'

    iPhone_4_64_GB = copy.deepcopy(iPhone_4_16_GB)
    iPhone_4_64_GB.name = 'iPhone 4 64 GB'
    iPhone_4_64_GB.details['memory'] = '64 GB'

    print(iPhone_4_64_GB.name, iPhone_4_64_GB.details)
    print(iPhone_4_32_GB.name, iPhone_4_32_GB.details)
    print(iPhone_4_16_GB.name, iPhone_4_16_GB.details)
