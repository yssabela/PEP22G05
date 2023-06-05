# i = 0                     # Initializarea unui counter i
#
# while i <= 10:             # Conditie verificata la fiecare iteratie de bucla
#     print(i)              # Se va afisa i-ul actual
#     i += 1                # Incrementarea lui i (aka i = i + 1) / Altfel, valoarea lui i va ramane 0 => rezulta in bucla infinita
# # ======================================================================================================================
# # CONTINUE - la intalnirea cuvantului cheie continue se va trece direct la urmatoarea iteratie de bucla
# # fara a continua cu executia restului de bucla pentru iteratia curenta
#
# i = 0
# while i < 10:
#     if i % 2 == 0:        # daca i este numar par
#         i += 1            # vom incrementa doar valoarea lui i pentru a evita o bucla infinita
#         continue          # se va intoarce la linia 71 => face din nou verificarea fara a executa restul buclei
#     print(i)              # va afisa numarul impar
#     i += 1                # vom incrementa valoarea lui i cu 1
# # Exemplu2
# # cuvant = "alfabet"
# # i = 0
#
# while i < len(cuvant):
#     if cuvant[i] == "a":
#         i += 1
#         continue
#     print(cuvant[i],end="")
#     i += 1

counter = 0
txt = input('Introduceti un cuvant: ')
litera = input('Introduceti o litera: ')
i = 0

# while i < len(txt):
#     if litera == txt[i]:
#         counter += 1
#     i += 1
# print(f'Litera apare de {counter} ori')

# for letter in txt:
#     if letter == litera:
#         counter += 1
# print(f'Litera apare de {counter} ori')

# for i in range(len(txt)):
#     if txt[i] == litera:
#         print(f'Litera {litera} se afla la indexul: ',i)

i = 0

while i < len(txt):
    if litera == txt[i]: print(f'Litera {litera} se afla la indexul: ',i)
    i += 1
