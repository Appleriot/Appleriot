class Car(object):
    """A simple attempt to make a car"""
    def __int__(self, make, model, year):
        """Instazile the attrubite of a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odemeter = 0
    def descibe(self):
        """Return a neatly formatted name"""
        long_name = f'{self.make} {self.model} {self.macuftaor}'
        return long_name.title()
    def read_odemeter(self):
        """Print a car mileage"""
        miles = self.odemeter
        print(f"My car mileage is {self.odemeter}.")

my_new_car = ('audi', 'a4', 2019)
print(f"My car is a {my_new_car}")
my_new_car.read_odemeter(miles)
