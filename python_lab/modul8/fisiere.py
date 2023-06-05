# File operations
#
# my_stream = open('my text.txt', mode='w')
# print(type(my_stream))
#
# my_stream.write('Hello Python')
# my_stream.close()  # also does my_stream_flush()
#
# # with statement
# with open('my text.txt', mode='w') as file:
#     file.write('Hello Python with')  # close is still called even in case of exception
#
# with open('my text.txt', mode='rb') as file:
#     result = file.read()
#
# # print(type(result))
# # print(result)  #this is a bytes object displayed as text
#
# import datetime
#
# my_date1 = datetime.datetime(year=2021, month=3, day=11)
# my_date2 = datetime.datetime(year=2020, month=5, day=10, minute=32)
#
# print(my_date1)
# print(my_date2)
# result = my_date1 - my_date2
# print(result)
# print(result.days)
# print(my_date2.minute)
#
# #get current date
#
# print(datetime.datetime.now())
#
# # compare dates
# print(my_date1>my_date1)

def a(x,y):
    return x+y
print(a(1,2))  #functia ramane in memorie; pe partea de garbage collection


b = lambda x,y: x + y  # si anonima astfel: lambda x,y: x + y
print(a(1,2))  # lambda nu ramane in memorie

def calcul(functie,numar):
    return functie(numar,numar)
print(calcul(a,9))
print(calcul(lambda x,y:x+y,8))

for i in range(100):
    print(calcul(lambda x, y: x + y+i, 8))

