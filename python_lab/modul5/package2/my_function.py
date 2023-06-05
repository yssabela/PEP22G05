nume = input('Introdu numele tau: ')
varsta = input('Cati ani ai? ')

def calcul_pers(numeF, varstaF):
    print('Hello! Numele tau este ' + numeF + ' si ai ' + varstaF + ' de ani.')
    ani = 0
    ani = int(varstaF)+20
    print('Peste 20 de ani vei avea '+ str(ani)+' de ani.')
    return

calcul_pers(nume, varsta)

print(__name__)

if __name__ == '__main__':
    print('Acesta este main.')

