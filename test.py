class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")


vehicle1 = Vehicle("Tesla", "Model S")
car1 = Car("Honda", "Civic", 2023)
vehicle1.display_info()
print("---")
car1.display_info()
