class Human:
    def __init__(self, name="Human"):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, humen):
        self.passengers.append(humen)

    def print_passegers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passengers in self.passengers:
                print(passengers.name)
            else:
                print(f"There are no passengers in {self.brand}")


nick = Human("Nick")
car = Auto("Volvo")
car.print_passegers_names()
car.add_passenger(nick)
car.print_passegers_names()
kate = Human("Kate")
car.add_passenger(kate)
car.print_passegers_names()
