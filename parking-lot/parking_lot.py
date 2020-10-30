# Imports
from enum import Enum

"""
- Multiple Floors
- Multiple Entry/Exit Points
- Timed Charges
- Multiple types of Spots(S, M, L, XL)
- For Each Floor and Whole Parking Lot show the left out spots


Actors in the Parking Lot
- Admin
- Manager
- Car

Classes in the Parking Lot
- People
- Admin
- Manager
- Car
- Order
- Charges
- Parking
- Floors
- Entry Point
- Exit Point
- SpotManager


Constants in Parking Lot-
- ChargesRange

Enums in Parking Lot
- SpotType
- OrderStatus
"""

class ChargeRange:
    def __init__(self, start_time, end_time, charge):
        self.start_time = 0
        self.end_time = 0
        self.charge = 0

class Constants:
    charges_range = [ChargeRange(0, 60, 5), 
                     ChargeRange(61, 120, 3.5),
                     ChargeRange(121, float('inf'), 2.5)]

class SpotType(Enum):
    S, M, L, XL = 1, 2, 3, 4

class OrderStatus(Enum):
    UnderProcess, Completed = 1, 2

class People:

    def __init__(self, name, address, contact):
        self.__name = name
        self.__address = address
        self.__contact = contact


class Manager(People):
    def __init__(self, name, address, contact, email, password):
        super().__init__(name, address, contact)

        self.__email = email
        self.__password = password

    def find_salary(self, *args):
        pass

    def create_order(self, *args):
        pass

    def find_car(self, *args):
        pass

    def compute_fine(self, *args):
        pass



class Admin(Manager):
    def __init__(self, name, address, contact, email, password):
        super().__init__(name, address, contact, email, password)


    def today_profit(self):
        pass


    def monthly_profit(self):
        pass


class Car:
    def __init__(self, car_type, license_number):
        self.__car_type = car_type
        self.__licence_number = license_number


class Order:
    def __init__(self, car, entry_point, spot):
        self.__car = car
        self.__entry_point = entry_point
        self.__spot = spot

    def compute_fine(self):
        pass

class OrderManager:
    def __init__(self):
        self.__orders = []
        self.__car_to_order = {}
        self.__day_to_order = {}
        self.__month_to_order = {}

    def create_order(self):
        pass


class Spot:
    def __init__(self, spot_type, charge_range):
        self.__spot_type = spot_type
        self.__charge_range = charge_range

class Floor:
    def __init__(self, floor_number):
        self.__floor_number = floot_number
        self.__spots = []


class ParkingDisplayBoard:
    def __init__(self,  )

class ParkingLot:
    def __init__(self, name, address, contact):
        self.__name = name
        self.__address = address
        self.__contact = contact
        self.__is_full = False
        self.__display_board = ParkingDisplayBoard()

    def create_ticket(self, vechile):
        pass