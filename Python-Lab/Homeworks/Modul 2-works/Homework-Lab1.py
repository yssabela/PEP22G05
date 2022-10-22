# Exercise  1

baza = int(input('Care este baza triunghiului?'))
inaltimea = int(input('Care este inaltimea triunghiului?'))
aria = (baza * inaltimea) / 2
print('Aria triunghiului este : ', aria)
print(type(aria))

# Exercise 2

number = 7110
password = int(input('password:'))
print(number == password)

if number == password:
    print('parola este corecta')
else:
    print('parola este incorecta')

# Exercise 3

a = 5
b = 10
media = (a + b) / 2
print('Media lui a si b este : ', media)
#
x = int(input('Introduceti un nr. intreg : '))
y = int(input('Introduceti al doilea nr. intreg : '))
impartirea = int(x / y)
print('Rezultatul impartirii este : ', impartirea)

x = int(input('Introduceti un nr intreg : '))
y = int(input('Introduceti un nr intreg : '))
puterea = x ** y
print('Rezultatul puterii este : ', puterea)

# Exercise 4

a = int(input('Venitul net este : '))

b = a * 50 / 100
print('Cheltuieli necesare', b)

c = a * 30 / 100
print('Cheltuieli recreative', c)

d = a * 20 / 100
print('Economii', d)
