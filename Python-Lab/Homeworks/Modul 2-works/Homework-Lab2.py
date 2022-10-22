# Exercise 1

a = ('Astazi ma duc la "facultate"')
print(a)

b = ('/*\*/*\*/*\ \n Python \n \./.\./.\./')
print(b)

print("P", "y", "t", "o", "n", sep="   ")

# Exercise 2

nume = input("Cum te numesti ?")
varsta = int(input("Ce varsta ai ?"))
x = 2022 - varsta
print("Ceau", nume, "! Deci te-ai nascut in", x, ".")

# Exercise 3

x = input("Introduceti un sir: ")
y = len(x)
print("Lungimea sirului este {0}".format(y))
print(f"Lungimea sirului este {y}")
print("Lungimea sirului este " + str(y))
print("Lungimea sirului este", y)

# Exercise 4

result = ' /-\ '.center(7)
print(result)
result = '//_\\\\'.center(7)
print(result)
result = '-------'.center(7)
print(result)
result = '\\\\_//'.center(7)
print(result)
result = '\_/'.center(7)
print(result)

#
print()

print('----'.center(8))
print('/    \\'.center(8))
print('/______\\'.center(8))

#
print()

print('*'.center(8))
print('***'.center(8))
print('*****'.center(8))
print('*******'.center(8))

# Exercise 5

cuvant = input('Introduceti un palindrom : ')
reverse = cuvant[::-1]
if (cuvant == reverse):
    print('Palindrom: True')
else:
    print('Palindrom: False')

# exercise 6

a = 'Hello Python'
b = 'Ana are mere'
c = 'Pizza Party'
result = a.split()
print(result[0], result[1], sep='_')
print(a.split()[0], a.split()[1], b.replace(' ', '_'), c, sep='_')
print(a.split()[0], a.split()[1], b.replace(' ', '_'), c, '.', sep='_')
print(a + '.', b.replace(' ', '_'), c, '.', sep='_')
print(a.split()[0] * 4, a.split()[1], b.replace(' ', '_'), c, sep='_')

# Exercise 7

a = 5.
b = 5
c = "ana"
print('Locatia lui a este : ', id(a))
print('Locatia lui b este : ', id(b))
print('Locatia lui c este : ', id(c))
print('Locatia lui a este : ', hex(id(a)))
print('Locatia lui b este : ', hex(id(b)))
print('Locatia lui c este : ', hex(id(c)))
print(type(a), type(b), type(c))
print('Type of a is : ', type(a))
print('Type of b is : ', type(b))
print('Type of c is : ', type(c))
