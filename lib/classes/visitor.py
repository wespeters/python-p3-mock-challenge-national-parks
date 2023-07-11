class Visitor:
    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self.__name = name
        else:
            raise Exception("Name must be a string and between 1 and 15 characters, inclusive")
        self.__trips = []

    @property
    def name(self):
        return self.__name

    def add_trip(self, trip):
        self.__trips.append(trip)

    def trips(self):
        return self.__trips

    def national_parks(self):
        return list(set(trip.national_park for trip in self.__trips))
