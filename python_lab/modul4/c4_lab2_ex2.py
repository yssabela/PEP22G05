my_numbers = []


def my_function():
    global my_numbers
    print('Introduceti numere.Cand sunteti gata,introduceti x.')

    while True:
        try:
            data = float(input('Numar: '))
            my_numbers.append(data)
        except ValueError:
            break

    meniul = ('''
  Meniu:
1. Media numerelor
2. Suma numerelor
3. Puterea numerelor din lista de numere
4. Iesire ''')
    print(meniul)

    response = input('Introduceti optiunea dvs: ')

    def suma():
        print('Suma este', sum(my_numbers))

    def medie():
        print('Media este', sum(my_numbers) / len(my_numbers))

    def putere():
        result1 = int(my_numbers[0])
        result2 = int(my_numbers[1])
        print('Primul nr la puterea celui de-al doilea este ', pow(result1, result2))



    if response == '1':
        medie()
    if response == '2':
        suma()
    elif response == '3':
        putere()
    elif response == '4':
        print('Ati iesit!')
    else:
        response != 'meniu'
        print('Alegeti din nou !')

    meniu = {
        "1": 'medie',
        "2": 'suma',
        "3": 'putere'
    }
my_function()
