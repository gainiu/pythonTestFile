# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name=restaurant_name
#         self.cuisine_type=cuisine_type
#         self.number_served=0

#     def describe_restaurant(self):
#         print('Restaurant name: '+self.restaurant_name)
#         print('Cuisine type: '+self.cuisine_type)

#     def open_restaurant(self):
#         print('The restaurant is in business.')

#     def set_number_served(self,numbers):
#         self.number_served=numbers

#     def increment_number_served(self,numbers):
#         self.number_served+=numbers

# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type,flavors):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors=flavors

#     def show_icecream(self):
#         print('We have many kinds of icecream:')
#         for flavor in self.flavors:
#             print('-'+flavor)

# my_icecream=IceCreamStand('ICE','icecream',['milk','chocolate','fruits'])
# my_icecream.describe_restaurant()
# my_icecream.show_icecream()

# class User():
#     def __init__(self,first_name,last_name,address):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.address=address

#     def describe_user(self):
#         print('Full name: '+self.first_name+' '+self.last_name)
#         print('Address: '+self.address)

#     def greet_user(self):
#         print('Hello~'+self.first_name+' '+self.last_name)

# class Admin(User):
#     def __init__(self,first_name,last_name,address):
#         super().__init__(first_name,last_name,address)
#         self.privilege=Privileges()

# class Privileges():
#     def __init__(self):
#         self.privileges=['can add post','can delete post','can ban user']

#     def show_privileges(self):
#         print('Admin has the following privileges: ')
#         for privilege in self.privileges:
#             print('-'+privilege)

# my_admin=Admin('xiao','min','china')
# my_admin.privilege.show_privileges()


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has '+str(self.odometer_reading)+' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a '+str(self.battery_size)+'-kwh battery.')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = 'This car can go approximately '+str(range)
        message += ' miles on a full charge.'
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
