# Exercise 2
def ridicare_la_putere(a, b):
    return int(a) ** int(b)


def putere() -> object:
    while True:
        data = input('Please provide number: ')
        if data == "q":
            break
        a, b = data.split(',')
        print('Result is', ridicare_la_putere(a, b))

putere()
