# # chr() and ord()
#
# print(ord('0'))
# print(ord('1'))
# print(ord('a'))
# print(ord('A'))
# print(chr(65))


# Trueish

a = "101"   # un string cu orice nr diferit de 0 este considerat intotdeauna True

print(a > '100')

if True:
    print('this will always be true')
if a:
    print('this will also always be true')

a = " " # un string gol este considerat intotdeauna False
if a:
    print('this will also always be false')
else:
    print('this will also always be false')

a = (0 + 2j)
if a:
    print('a is True')
else:
    print('a is False')

