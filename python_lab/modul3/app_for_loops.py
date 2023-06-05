# For loops
a = 'my_string'
for i in a:
    print(i)

# poate fi descompus orice obiect care este iterabil
result = range(10)
print(type(result))
print(result)
print(result.__iter__())

for i in result:
    print(i)


# while loop
a = 100
while a < 200:
    print('To infinity')
    a += 1
    if a % 101:
        break
        print('after break')


# Exercise

my_var = 3.3
my_list = ['a', 1, True, my_var]
my_list.__iter__()

for obj in my_list:
    print(obj)
print('adding to list')
my_list.append([])

for obj in my_list:
    print(obj)

print(f'first object is: {my_list[-1]}')

my_list.extend([1,2,3])
for obj in my_list:
    print(obj)
print(my_list)
print('Response is:',my_list.extend([1,2,3])) # but initial list is modified
print(my_list)


