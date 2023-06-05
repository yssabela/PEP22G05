import utiles

def magazin():
    meniu = ''' Meniu:
1. Vizualizare stoc
2. Adaugare produs
3. Stergere produs
4. Iesire
    '''

    stoc = {}

    while True:
        response = input(meniu).strip()
        if response == '1':
            utiles.vizualizare_stoc(stoc)
        elif response == '2':
            utiles.adaugare_produs(stoc)
        elif response == '3':
            utiles.stergere_produs(stoc)
        elif response == '4':
            break
        else:
            print('Nu ai introdus o val.valida')


if __name__ == '__main__':
    print(magazin())
