from classes.visitor import Visitor
from classes.national_park import NationalPark

class Trip:
    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise Exception("Visitor must be of type Visitor")
        if not isinstance(national_park, NationalPark):
            raise Exception("NationalPark must be of type NationalPark")

        self.__visitor = visitor
        self.__national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        visitor.add_trip(self)
        national_park.add_trip(self)

    @property
    def visitor(self):
        return self.__visitor

    @visitor.setter
    def visitor(self, value):
        if not isinstance(value, Visitor):
            raise Exception("Visitor must be of type Visitor")
        self.__visitor = value

    @property
    def national_park(self):
        return self.__national_park

    @national_park.setter
    def national_park(self, value):
        if not isinstance(value, NationalPark):
            raise Exception("NationalPark must be of type NationalPark")
        self.__national_park = value
