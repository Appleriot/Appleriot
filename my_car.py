from car import Car, eletric_car

my_new_car = Car('audi', 'a4', 2019)
print(f"My car is a {my_new_car.descibe()}")

my_beelte = eletric_car('telsa', 'au', '2020')
print(my_beelte.descibe())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
