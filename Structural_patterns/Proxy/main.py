import json
import logging
from abc import ABC, abstractmethod


class Driver:

    def __init__(self, name: str, image=None, rating=None):
        self.__name = name
        self.__image = image
        self.__rating = rating

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: int):
        self.__name = name

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image: int):
        self.__image = image

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating: int):
        self.__rating = rating


class Drivers:
    def __init__(self, json_file="drivers.json"):
        self.__json_file = json_file

        with open(self.__json_file, "r") as read_file:
            drivers_from_json = json.load(read_file)

        self.__drivers = drivers_from_json['drivers']

    @property
    def drivers(self):
        return self.__drivers

    @drivers.setter
    def drivers(self, driver: Driver):
        self.__drivers.update(driver)
        with open(self.__json_file, "w") as write_file:
            json.dump(self.__drivers, write_file)


class Car:

    def __init__(self, id: int, plate: str, color: str, model: str, driver: Driver):
        self.__id = id
        self.__plate = plate
        self.__color = color
        self.__model = model
        self.__driver = driver

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def plate(self):
        return self.__plate

    @plate.setter
    def plate(self, plate: str):
        self.__plate = plate

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def model(self):
        return self.__plate

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver: str):
        self.__driver = driver


class TaxiPark:

    def __init__(self, cars: dict = None, json_file="cars.json"):
        self.__json_file = json_file
        self.__cars = cars

        with open(self.__json_file, "r") as read_file:
            cars_from_json = json.load(read_file)

        self.__cars = cars_from_json['cars']

    @property
    def cars(self):
        return self.__cars

    @cars.setter
    def cars(self, car: Car):
        self.__cars.update(car)
        with open(self.__json_file, "w") as write_file:
            json.dump(self.__cars, write_file)


class CarTrekking:

    def __init__(self):
        self.__geo = 'Mechnikova St.'

    @property
    def geo(self):
        return self.__geo


class ITaxiApp(ABC):

    @abstractmethod
    def make_order(self, type_of_taxi):
        pass


class TaxiApp(ITaxiApp):

    def __init__(self):
        self.__taxi_park = TaxiPark()
        self.__taxi_drivers = Drivers()
        self.__trekking = CarTrekking()

    def feedback(self):
        pass

    def make_order(self, type_of_taxi) -> list:
        driver, car = self.__find_driver(type_of_taxi)
        if driver is not None:
            print(f"Водитель найден, он сейчас находится на {self.__trekking.geo}")
            self.__show_result(driver, car)
        return [driver, car]

    def __find_driver(self, type_of_taxi):
        cars = self.__taxi_park.cars
        drivers = self.__taxi_drivers.drivers

        for i in range(len(cars)):
            if cars[i]["type_of_taxi"] == type_of_taxi:
                for j in range(len(drivers)):
                    if drivers[j]["name"] == cars[i]["driver"]:
                        return drivers[j], cars[i]

    @staticmethod
    def __show_result(driver: dict, car: dict):
        print('-' * 5, 'Driver Info', '-' * 5)
        for key, value in driver.items():
            if key != 'id':
                print(key, value)
        print('-' * 5, 'Car Info', '-' * 5)
        for key, value in car.items():
            if key != 'id' and key != 'driver':
                print(key, value)


class LogProxy(ITaxiApp):
    logging.basicConfig(filename='log_info.log', encoding='utf-8', level=logging.DEBUG)

    def __init__(self):
        self.__app = TaxiApp()

    def make_order(self, type_of_taxi):
        logging.info(f'-----Make order-----')
        order = self.__app.make_order(type_of_taxi)
        logging.info(order)
        return order


class Client:

    def __init__(self):
        self.__app = LogProxy()

    '''
    Universal, VIP, Minibus
    '''

    def use_app(self):
        return self.__app.make_order("VIP")


if __name__ == "__main__":
    client = Client()
    client.use_app()
