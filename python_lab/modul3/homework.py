# Exercise 1

cnp = input('Introduceti primele 7 cifre din CNP: ')
cnp_an = int(cnp[1:3])
cnp_luna = int(cnp[3:5])
cnp_zi = int(cnp[5:7])

if cnp_an > 50:
    cnp_an = 1900 + cnp_an
else:
    cnp_an = 2000 + cnp_an

if ((2022 - cnp_an) > 18):
    print('Aveti peste 18 ani.')
elif (2022 - cnp_an == 18):
    if (cnp_luna < 10):
        print('Ati implinit 18 ani anul acesta.')
    elif (cnp_luna == 10):
        if (cnp_zi <= 20):
            print('Ati implinit 18 ani luna acesta.')
        else:
            print('Nu aveti peste 18 ani.')
    else:
        print('Nu aveti peste 18 ani.')
else:
    print('Nu aveti peste 18 ani.')

print(cnp_zi, cnp_luna, cnp_an)

# Exercise 2

num = range(int(input('Introduceti un numar:')))

for i in num:
    result = i % 2
    if result == 0:
        print(i)

# Exercise 3

cappuccino = 4
espresso = 3.5
print(f'cappuccino...{cappuccino} lei')
print(f'espresso...{espresso} lei')
optiune = int(input('Ce optiune alegeti?[1,2]').strip())
response = int(input('Selectati un nr. intre 1 to 3'))
while not (1 <= response <= 3):
    response = int(input('Reintroduceti un numar intre 1 si 3 : '))
bancnota = int(input('Introduceti o bancnota,[5:10]'))

if optiune == 1:
    result = bancnota - cappuccino
elif optiune == 2:
    result = bancnota - espresso
else:
    result = bancnota
print(f'restul tau este {result}')


# Exercise 4

i = 0
while i < 3:
    passw = input("Introduceti parola:")
    if passw == "7788":
        print("Access permis!")
        break
    else:
        print("Parola gresita. Mai incercati.")
        i += 1
else:
    print("PC-ul este blocat pentru urmatoarele 30 minute!!!")

### second method

parola=7788
b=range(3)
for i in b:
    a = int(input('Introduceti o parola: '))
    if(a==parola):
        print('Acces permis')
        break
    else:
        print('Parola gresita. mai incercati.')
else:
    print('Acccount locked')

# Exercise 5

lista = ['Masa', 5, 'Scaun', 4.5, [5, 6, 7], 8]
print('Tipul obiectului Masa este',type(lista[0]).__name__)
print('Tipul obiectului 5 este',type(lista[1]).__name__)
print('Tipul obiectului Scaun este',type(lista[2]).__name__)
print('Tipul obiectului 4.5 este',type(lista[3]).__name__)
print('Tipul obiectului [5,6,7] este',type(lista[4]).__name__)
print('Tipul obiectului 8 este',type(lista[5]).__name__)

# Exercise 6

cuvant = input('Introduceti un cuvant(fara majuscule): ')
print('r apare de', cuvant.count('r'), 'ori')

# Exercise 7

lista = input('Introduceti lista de taskuri: ')
lista_taskuri = lista.split(',')

for task in lista_taskuri.copy():
    if lista_taskuri.count(task) >= 1:
        lista_taskuri.remove(task)
print(lista_taskuri)
