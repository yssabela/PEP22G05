# un joc similar cu piatra-foarfece-hartie

import random  # se genereaza importul

def my_game():  # se defineste o functie my_game
    states = {'p': 'piatra', 'h': 'hartie', 'f': 'foarfeca'}
    results = {'piatra-foarfeca': True, 'foarfeca-hartie': True, 'hartie-piatra': True}

    options = list(states.keys())
    name = input('Introduceti numele: ')
    option = input(f'Introduceti optiune: {states}')

    if option == 'q':
        print('Ai parasit jocul! ')
        quit()
    else:  # mai simplu s-ar rezolva cu random choice
        selection = random.randint(0, 2)  # se itereaza optiunea serverul
        selected = options[selection]  # aici este optiunea serverului
        print(selected)

    if option not in options:  # trebuie sa ne asiguram ca este o optiune valida
        print('eroare')  # verificam pe option ca se afla intr-o lista de optiuni

    print(f'> {name}: {states[option]}')  # printam raspunsul utilizatorului
    print(f'> Server: {states[selected]}')  # printam raspunsul serverului

    if states[option] == states[
        selected]:  # nu putem compara pana nu definim inca un dictionar cu rezultatul combinatiilor.(vezi mai sus)
        print('Incearca inca o data')
        return None

    try:
        results[f'{states[option]} == {states[selected]}']    # pt cazurile in care un element nu este in dictionarul de result
        print('Ai castigat!')
    except:
        print('Serverul a castigat')


# se creaza input de nume si optiunea aleasa
# cu if se efectueaza conditia de a iesi din program
# cu else serverul prezinta optiunea lui
# de definit regula de joc
# print castigatorul : se poate face cu conditiile if,elif si else ,dar se mai poate face printr-o metoda mai usoara.


my_game()
