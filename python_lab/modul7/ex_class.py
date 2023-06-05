# clase,instantele clasei,atributele clasei si metode.
# cand rulam codul observam ca ele sunt obiecte/instante ale clasei Robot
# functionalitatile sunt metodele folosite in interiorul claselor sau sunt functiile din interiorul claselor
# trebuie sa gandim astfel: ce functionalitate poate avea o instanta a clasei Robot?

class Robot:
    garantie = 10
    number_of_robots = 0
    def __init__(self,nume,serial_number,hardware,software,age,sleep):
        self.nume =  nume
        self.serial_number = serial_number
        self.hardware = hardware
        self.software = software
        self.sleep = sleep
        self.age = age
        Robot.number_of_robots +=1

    def turn_on(self):
        if self.sleep == False:  # ca sa pornim robotul trebuie sa modificam sleep
            return f'{self.nume} is already running'
        else:
            self.sleep = False
            return f'{self.nume} is sleeping ?'

    def end_of_life(self):
        if self.age > self.garantie:
            print(f'{self.nume} is end of life.')
        else:
            print(f'{self.nume} has {self.garantie-self.age} years till end of life.')

print(Robot.number_of_robots)

r1 = Robot('Split','12333','i5','Python',11,True)  # instanta clasei robot
r2 = Robot('Chiller','22333','i5','C++',3,False)

print(Robot.number_of_robots)

print(r1.end_of_life())
print(r2.end_of_life())


# print(r1.serial_number)
# print(r2.serial_number)
# print(r1.sleep) # sa vedem daca robotul doarme
# print(r2.sleep)
# print(r1.turn_on()) # apelarea metodei turn_on sa vedem daca s-a modificat prin intermediul instantei
# print(Robot.turn_on(r1)) # apelarea metodei turn_on prin intermediul clasei
# print(r1.sleep)
# print(r2.sleep)


#print(Robot.garantie)
# print('namespace before',r1.__dict__)
# r1.garantie = 3
# print('namespace after',r1.__dict__)
# print('namespece of class',Robot.__dict__)








