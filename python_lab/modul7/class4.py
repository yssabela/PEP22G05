class A():
    attr1 = 'my_text'
    attr2 = 10


a = A()
#check attribute
print(hasattr(a, 'attr1'))
# get value from attribute
print(getattr(a, 'attr3', 'abcd'))
print(getattr(a, 'attr1'))
# setting an attribute
for i in range(100):
    setattr(a, f'attr{i}', f'{i + 1}')
# print(a.attr1)
# print(a.attr2)
# print(a.attr3)
#
# print(a.__setattr__('new_attr','100'))
# print(a.new_attr)
# print(a.__getattribute__('new_attr'))

# create object and set attributes from input:

# while True:
#     response = input('Enter attributes and values: ')
#     if response == 'q':
#         break
#     attr1,val1 = response.split(',')
#     a.__setattr__(attr1,val1)
#     print(dir(a))