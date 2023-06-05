valoare = input('Introdu un numar: ')

def calcul_suma(valoare):
    suma = 0
    for i in range(int(valoare) + 1):
        suma = suma + i
    return suma

rezultat = str(calcul_suma(valoare))
print('Suma pentru ' + valoare + ' este ' + rezultat)

#
# def calcul_persoana(nume,varsta):
#     print(f'Ok, te numesti {nume} si ai {varsta} ani')
#     ani = 0
#     ani = int(varsta) + 20
#     print('Peste 20 de ani vei avea '+ str(ani))
#     return
#
# nume = input('Salut! Spune-mi cum te numesti: ')
# varsta = input('Cati ani ai ? ')
#
# calcul_persoana(nume,varsta)
