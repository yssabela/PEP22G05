class MyCarFactory:
    windows_no = 4

    def __init__(self,windows):
        self.windows_no= windows


car1 = MyCarFactory(5)
print('Car1 windows :', car1.windows_no)

##########################

class my_car():
    doors_no = 3
    def __init__(self, doors):
        self.doors_no = doors
my_new_car = my_car(5)
print(my_new_car.doors_no)