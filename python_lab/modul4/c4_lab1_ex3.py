pc1 = {'admin1': 'passme1'}
pc2 = {'admin2': 'passme2'}
pc3 = {'admin3': 'passme3'}


def calculator():
    data = {}
    for i in range(1, 4):
        user = input(f'Introduceti utilizatorul pc-ului : {i}')
        parola = input(f'Introduceti parola pc-ului : {i}')
        data[user] = parola
        #data.update({user:parola})
    for key,value in data.items():
        print(key,'->',value)

calculator()
