# exception classes

# import time
# from time import sleep
#
#
# class MyException(BaseException):
#     def __str__(self, *args, **kwargs):
#         # print(self.args)
#         # print(self.kwargs) # no kwargs
#         return f'{self.__class__.__name__, self.args, self.__traceback__}'
#
#
# try:
#     if time.time() > 150000.0:
#         raise MyException('test', 'test2')
# except Exception:
#     print('Test Exception')
# except MyException as obj1:
#     print(obj1)
#     print('success')
#     raise
#
# keyboard interrupt should not be treated
# try:
#     while True:
#         sleep(1)
#         print('in loop')
# except KeyboardInterrupt:
#     while True:
#         sleep(1)
#         print('new loop')
# # AttributeError()


# # Generators (general working)
#
# my_generator = range(2)
# print(type(my_generator))
# my_iterator = my_generator.__iter__()
# print(type(my_iterator))
# new_iterator = my_iterator.__iter__()
#
# print(id(new_iterator), id(my_iterator))
#
# print(my_iterator.__next__())
# # print(next(my_iterator))
# print(next(new_iterator))
# # print(next(my_iterator))
#
# print("#" * 80)
#
#
# # generator functions -> return generators
# def my_generator(number):
#     for i in range(number):
#         yield i
#     yield number + 1
#
#
# print(type(my_generator))
# my_gen_obj = my_generator(10)
# print(type(my_gen_obj))
# print(my_gen_obj.__next__())
# print(my_gen_obj.__next__())
# print(my_gen_obj.__next__())
# for i in range(7):
#     print('in for loop', my_gen_obj.__next__())
#
# my_new_gen = (i for i in range(10))
# print(my_new_gen)
# for i in range(10):
#     print('in new for loop', my_new_gen.__next__())


#  Iterators classes - return iterators
#
# class MyIterator:
#
#     def __init__(self, number):
#         self.number = list(range(number))
#
#     def __next__(self):
#         try:
#             return self.number.pop(0)
#         except IndexError:
#              raise StopIteration
#
#
class MyIterator:

    def __init__(self, number):
        self.number = number
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == self.number:
            raise StopIteration
        return self.counter
#
#
# my_iterator = MyIterator(3)
# print(my_iterator.__next__())
# print(my_iterator.__next__())
# # print(my_iterator.__next__())
# new_iterator = my_iterator.__iter__()
# print(id(new_iterator), id(my_iterator))
#
# for i in my_iterator:
#     print(i)

class MyInt():
    number = 0

    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return MyIterator(self.number)
        # return (i for i in range(self.number))


my_number = MyInt(10)

for number in my_number:
    print(number)