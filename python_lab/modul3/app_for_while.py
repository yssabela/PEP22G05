# continue

my_str = 'abcdefg'

for letter in my_str:
    print('before continue')
    if letter == 'd':
        continue  # this will stop current iteration
    if letter == 'f':
        break  # this will stop for loop
    print(letter)

# else -  keyword

my_str = 'abcdefg'

for letter in my_str:
    print('before continue')
    if letter == 'd':
        continue  # this will stop current iteration
    print(letter)
else:
    print('All is done')  # this will never get executed if break is encountered.

    ############
my_number = 0

while my_number < 5:
    print(my_number)
    if my_number == 3:
        break
    my_number += 1  # este o forma prescurtata a
else:
    print('all done while')

# Lists
my_var = 3.3
my_list = ['a', 1, True, my_var]
my_list.__iter__()

for obj in my_list:
    print(obj)

# informatii pierdute- de continuat

# modifying object

a = 'name : {}'
print(f'Initial ID:{id(a)}')
result = a.format('abcd')
print('Identity of objects:',id(a),id(result))

b= ['name: {}']
print(f'Initial ID:{id(b)}')
result = b.append('abcd')
print('Identity of objects:',id(b),id(result))
print(b) #listele sunt mutable

# mutable objects in loops

my_new_list = list('random')
for letter in my_new_list:
    my_new_list.append('a')
    print(letter) # duce la o infinitate de litere

# sau
for letter in my_new_list:
    my_new_list.pop()
    print(letter) # opreste infinitatea

#sau

for letter in my_new_list.copy():
    my_new_list.pop()
    print(letter)  # copy of the list

#

my_list = ["Masa", 5, "Scaun", 4.5, [5, 6, 7], 8]
for elem in my_list:
    print("Tipul", elem, "este :", type(elem))
    if (type(elem) == list):
        for el in elem:
            print("    Nivelul 2:", el, "este", type(el))