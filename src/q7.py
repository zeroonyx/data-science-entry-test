class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    #declare class attributes
    year = None
    make = None
    model = None
    #initialize attributes in the __init__ method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    #method to describe the car
    def describe_car(self):
        print(self.year, self.make, self.model)

# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
#create an instance of the Car class
car1 = Car("Toyota", "Corolla", 2020)
#call the describe_car method
car1.describe_car()
