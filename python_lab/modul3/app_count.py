cuvant = input('Introduceti un cuvant(fara majuscule): ')
print('r apare de', cuvant.count('r'), 'ori')

#

x = list(cuvant)
y=x.count('a')
print(y)

x = list(cuvant)
y=x.count(x[0])  #index de x
print(y)