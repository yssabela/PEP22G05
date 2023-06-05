"""
A production facility needs an iterable object to keep track off car warranty.
Each car have a int serial and datetime object for when the car was produced.
Iterating the object will return all cars that are still covered by 3 years warranty (serial, <timedelta>)
1) 40p: Definition
    a) 10p: Basic class structure of objects
    b) 10p: Basic class structure of iterator
    c) 10p: Method to add sold cars.
    d) 10p: Method to print cars not covered by warranty
2) 40p: Execution:
    a) 10p: Create instance of your shop
    b) 10p: Call method to add (sell) car (serial, <datetime>))
        - 1588, 20 Jan 2019 10:30:32
        - 1692, 20 Jan 2021 9:20:25
        - 1994, 20 Jan 2022 9:10:30
    c) 10p: Call method to return expired warranty (serial, <datetime>))
    d) 10p: Iterate the created object and write each care covered by warranty in a file
3) 20p: Documenting:
   a) 5p: type hints for arguments
   b) 5p: module documentation
   c) 5p: class documentation for all classes
   d) 5p: method documentation for all methods
"""
from datetime import datetime, timedelta

class CarsIterator:
    """iterator for warranty cars"""
    def __init__(self, my_cars: dict):
        self.car = my_cars
        self.car_warranty = []
        for serie, data in my_cars.items():
            if (datetime.now()- data).days < 3* 365:
                self.car_warranty.append((serie,data))

    def __iter__(self):
        return self

    def __next__(self):
        if self.car_warranty:
            return self.car_warranty.pop()
        else:
            raise StopIteration


class Cars:
    """class for tracking cars warranty"""

    production = {}

    def __iter__(self):
        """ iterating through production """
        return CarsIterator(self.production)


    def __init__(self):
        pass

    def add_product(self, serial:int, start_warranty:datetime):
        """ add serials in production cars"""
        self.production.update({serial: start_warranty})

    def end_warranty(self):
        """ print expired warranty """
        for serie, data in self.production.items():
            warranty_time = datetime.now() - data
            if warranty_time.days >= 3 * 365:
                print(warranty_time)



car = Cars()
car.add_product(1588,datetime(2019, 1, 20, 10, 30, 32))
car.add_product(1692,datetime(2021, 1, 20, 9, 20, 25))
car.add_product(1994, datetime(2022, 1, 20, 9, 10, 30))
print(car.production)


with open('Warranty.txt', 'w') as file:
    for item in car:
        file.write(str(item) + '\n')