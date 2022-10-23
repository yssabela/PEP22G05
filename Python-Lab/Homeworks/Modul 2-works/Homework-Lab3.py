# de cautat : cum am putea printa numele variabilei in interiorul unui string ???
my_var = 'My string'
result1 = f'{my_var=}'
print(result1)
# print numele variabilei folosind f-string :
result2 = f'{my_var=}'.split('=')[0]
print(result2)

# Exercise 1

parola = input('Your password is : ')
print(parola == 'Passme1n')

# Exercise 2

a = input('Your first name is : ')
b = input('Your second name is : ')
c = len(a)
d = len(b)

print('Length of your first name is: ', c)
print(a == b)
print(c == d)
print(a[0])
print(a[-1::-1])

# Exercise 3

name1 = input('Introduceti un nume de referinta : ')
name2 = input('Introduceti un alt nume : ')
lungime = len(name1)

print('Lungimea numelui de referinta este :', lungime)
print('Numele de referinta este acelasi cu numele dat :', name1 == name2)
print('Numele de referinta este mai lung decat numele dat :', name1 > name2)
print('Initiala numelui de referinta este :', name1[0])
print('Numele de referinta inversat este :', name1[::-1])

num = int(input('Number: '))
print('Introduceti un numar :', num)
print(name1 * num)

# Exercise 4

my_var = '\n A\n n\n a\n n\n a\n s\n'
print(my_var)

my_var = 'Ananas'
print(my_var[0:3])
print(my_var[3:6])
print(my_var[0:2], my_var[2:5], my_var[-1], sep=":")
print(my_var[0:3], my_var[3:5], my_var[-1], sep="_")
print(my_var[1:3] * 8)

# Suplimentar
# 1

my_word = input('Introduceti un cuvant :')
reverse = my_word[::-1]
result = my_word.title()
print(result)

if my_word == reverse:
    print(True)
elif my_word == result:
    print(True)
else:
    print(False)

# 2

sir = input('Introduceti un sir :')
result1 = sir.capitalize()
result2 = sir.upper()

if sir == result1:
    print('Sirul incepe cu o majuscula: ', True)
elif sir == result2:
    print('Sirul incepe cu o majuscula: ', True)
else:
    print('Sirul nu incepe cu o majuscula: ', False)
