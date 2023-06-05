import class3
import sys

from class3 import Haine
from class3 import Accesorii
from class3 import Incaltaminte

bluze = Haine("bluze", 10, 5)
produse = []
h1 = Haine("Pantaloni", 100, 3)
a1 = Accesorii("Bratara", 100, 4, 'argint')
produse.append(h1)
produse.append(a1)


def vizualizare(produse):
    for produs in produse:
        print(produs)


def add_product(produse):
    argumente = {}
    products = {'1': Haine, '2': Accesorii, '3': Incaltaminte}
    product_selector = input("What is the category\n 1: Haine\n 2: Accesorii\n 3: Incaltaminte")
    nume = input('nume:')
    pret = int(input('pret:'))
    stoc = int(input('stock:'))
    if product_selector == '2':
        material = input('material:')
        argumente.update({"material": material})
    elif product_selector == '3':
        culoare = input('culoare: ')
        argumente.update({'culoare': culoare})
    my_class = products[product_selector]
    try:
        new_product = my_class(nume, pret, stoc, **argumente)
    except:
        print('something is wrong')
    else:
        produse.append(new_product)


def afisare_categorii():
    # import inspect
    # clase = [nume_clasa for nume_clasa, nume_obiect in inspect.getmembers(sys.modules['class3']) if
    #          inspect.isclass(nume_obiect)]
    # print('Categoriile sunt: ')
    # for elem in clase:
    #     print(f'__{elem}')
    print(dir(class3))


def meniu():
    meniu = {"1": afisare_categorii, "2": sub_meniu, "3": quit}
    while True:
        optiune = input("Optiuni:\n1.Afisare categorii \n2.Sub_meniu \n3.Iesire\n").strip()
        if optiune in meniu:
            meniu[optiune]()
        # if optiune == '2':
        #     meniu[optiune]()
        # if optiune == '1':
        #     pass
        # if optiune == '3':
        #     break


def sub_meniu():
    meniu = {"1": add_product, "2": vizualizare, "3": quit}
    while True:
        optiune = input('Optiuni:\n1.Adaugare produs\n2.Vizualizati\n3.Iesire\n').strip()
        try:
            # action_meniu = meniu[optiune]
            if optiune == '2' or optiune == '1':
                meniu[optiune](produse)
            elif optiune == '3':
                meniu[optiune]()
        except KeyError:
            print('Incorrect value! try again... ')


meniu()

