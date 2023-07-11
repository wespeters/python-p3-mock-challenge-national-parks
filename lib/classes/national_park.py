class NationalPark:
    def __init__(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception("Name must be a string")
        self.__trips = []

    @property
    def name(self):
        return self.__name

    def add_trip(self, trip):
        self.__trips.append(trip)

    def trips(self):
        return self.__trips

    def visitors(self):
        return list(set(trip.visitor for trip in self.__trips))

    def total_visits(self):
        return len(self.__trips)

    def best_visitor(self):
        visitors = [trip.visitor for trip in self.__trips]
        return max(visitors, key=visitors.count)
