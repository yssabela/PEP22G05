#3. Exercitiu suplimentar lib2to3
#var=input().split(",") utilizatorul alege numerele
#numerele_castigatoare = [4,12,31,17,22,25 ]
#
#print(var)
"""
pas 1: input utilizator ca si lista de numere
pas 2: transfomarea si validarea fiecarui element din lista
pas 3: selectarea numerelor corecte (de la 1 la 49) + bucla pt validarea
numerelor corecte, calcularea si excluderea dublurilor
pas 4: declararea castigurilor in fct de numarul de elemente ghicite
pas 5: calcularea si excluderea dublurilor
"""
# n=int(input())
#pseu
"""
creem o lista goala in care vom introduce numerele de la utilizator
*CAT TIMP nu avem inca 6 numere valide
REEM INPUT de la utilizator cu un string de numere
DACA este numeric, transformam inputul din string in lista
DACA nr este valabil(nu este dublura, nu este deja in lista, este intre 1-
49, daca este mmuneric ) il introducem in lista
*
PENTRU fiecare element din lista de nr castigatoare verificam daca il
intalnim in lista creata de utilizator si incrementam valoarea unui counter
DACA counter-ul are valoarea de 2, castigul este de 50 lei
DACA counter-ul are valoarea de 3 sau 4, castigul este de 500 lei
DACA counter-ul are valoarea de 5, castigul este de 1000 lei
DACA counter-ul are valoarea de 6, castigul este de 500 lei
="""
# numere_alese = []
#
#
# while True:
# numar = input("Introduceti un numar: ")
#
# if numar.isdigit():
# numar=int(numar)
# if numar >= 1 and numar <= 49:
# if numar not in numere_alese:
# numere_alese.append(numar)
#
# print(numere_alese)
# if len(numere_alese) == 6:
#
#
# break
#
# print (numere_alese)
#
# numere_castigatoare = [4,12,31,17,22,25]
#
# numere_ghicite = []
# var = 0
# for nr in numere_castigatoare:
# print (nr)
# if nr in numere_alese:
# numere_ghicite.append(nr)
# var += 1
# print(var)
#
# print("Numerele castigatoare sunt:", numere_castigatoare)
# print("Numerele alese sunt: ", numere_alese)
# print("Numerele ghicite sunt: ",numere_ghicite)
#
# dict_castig = {
# 2: "50",
# 3: "500",
# 4: "500",
# 5: "1000",
# 6: "5000"
# }
# if var in dict_castig:
# print("ati castigat", dict_castig[var],"RON!")
# Ati castigat 50 lei
""""
Creem o lista goala care va contine numerele valide
# a. - Validarea numerelor
1. Introducem sir de la utilizator, separate prin virgula - utilizam
*split
2. Transformam sirul in lista - PENTRU fiecare el din lista verificam DACA
:
- sunt numerice
- au range intre 0 si 100
*DACA conditiile sunt indeplinite il adaugam intr-o lista noua
# b. - Meniu (*while true)
1. Afisam meniul - *print
2.1 Daca utilizatorul alege optiunea ( fiecare nr la puterea Y):
- Facem o lista goala pentru rezultate
- setam input pentru Y
- PENTRU FIECARE nr. in lista: nr**Y si il adaugam in lista goala
2.2 Daca utilizatorul alege optiunea 2
- Facem suma tuturor nr. din lista - *sum(lista) lista data ca
parametru *cond - lista sa aibe doar stringuri
2.3 Daca utilizatoul alege optiunea 3
- Facem o lista goala pentru rezultate
- Setam input pentru Y - > Il transformam in *float
- PENTRU FIECARE nr. in lista: nr*Y( se inmulteste - nu se rid la
putere) si il adaugam in lista goala
2.4 Daca utilizatorul alege optiunea 4 ( Iesire ):
- Folosim *break
"""