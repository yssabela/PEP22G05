empty_dict = {}
my_dict = {'key1': 'value3', 3.14: 'True', 'Py': 1}
my_dict[1] = False
print(my_dict)

# methods
result = my_dict.pop(1)
print(result)
print(my_dict)

result = my_dict.update({'key1': 'value3'})
print(my_dict)
my_dict.__iter__()

#
for item in my_dict:  # keys are iterated
    print(item)

print('listing values')
for item in my_dict.keys(): # keys are iterated
    print(item)

print('listing values')
for item in my_dict.values():  # value are iterated
    print(item)

print('listing value')
for item in my_dict.items(): # items are iterated
    print(item)

print('listing value in separate variables')
for key,value in my_dict.keys():
    print(f'key{key},value{value}')