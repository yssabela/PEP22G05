angajat = {'nume': 'Popescu', 'prenume': 'Ion', 'job': 'inginer', 'salariu': 10000}
print(angajat)
print(angajat['salariu'])

if 'manager' in angajat:
    print(angajat['manager'])
else:
    print('cheie inexistenta')

print(dir(angajat))
print(help(dict.get))

# adaugare cheie

angajat['manager'] = 'Ivan'
print(angajat)
print(angajat.get('manager', 'Cheie inexistenta'))

# adaugare valori dintr-un dictionar in altul

d = {'email': angajat['nume'] + '.' + angajat['prenume'] + '@company.com', 'telefon': '111:222:333'}
angajat.update(d)
print(angajat)

angajat.pop('job')
print(angajat)

print(angajat.keys())
for key in angajat.keys():
    print(key)
print()
for value in angajat.values():
    print(value)

print()

print(angajat.items())
for key,value in angajat.items():
    print(str(key)+'===>'+str(value))
