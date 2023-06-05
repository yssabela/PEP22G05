import time


class Car:
    color = 'yellow'
    motors = ['fw-2KW-engine']
    lights = 'off'

    def __init__(self, color='blue'):
        # print(self.color)
        # wheels = 4 # this is local to __init__
        self.wheels = 4
        self.construction_date = time.time()
        self.color = color

    def start_car(self):
        print('Brum..brum')
        self.lights = 'on'

    @staticmethod
    def factorial(number):
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

    def __eq__(self, other):
        print(f'{self.construction_date},{other.construction_date}')
        if self.color == other.color and self.wheels == other.wheels:
            return True
        else:
            return False

    def __str__(self):
        return f'data ={self.construction_date}, culoare = {self.color},nume ={self.name}'


car1 = Car()
car1.name = 'Audi'
car2 = Car()

print(car1)

#data de fabricatie,culoarea,numele

# time.sleep(0.1)
# print(car1 == car2)
# car2.wheels = 5
# print(car1 == car2)

# print('Color before changes ',car1.color)
# print(Car.__init__(car1, color='red'))
# print('Color after changes ',car1.color)
#
# print('Lights before start', car1.lights)
# car1.start_car()
# print('Lights after start', car1.lights)
#
# print(car1.factorial(5))

# car1 = Car('green')
# print(type(car1))
# print(car1.color)
#
# time.sleep(1)
#
# car2 = Car()
# print(type(car2))
# print(car2.color)
#
# car2.color = 'blue'
# print("Car2 is :", car2.color)
# print("Car1 is :", car1.color)
#
# car2.motors.append("rw-4KW-engine")
# print("Car2 motor is :", car2.motors)
# print("Car1 motor is :", car1.motors)
#
# car2.wheels = 5
# print("Car2 wheels is :", car2.wheels)
# print("Car1 wheels is :", car1.wheels)
#
# print("Car2 date is :", car2.construction_date)
# print("Car1 date is :", car1.construction_date)
