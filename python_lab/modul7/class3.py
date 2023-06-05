class Haine:
    nume = ''
    pret = 0
    stoc = 0

    def __init__(self, nume, pret, stoc, **kwargs):
        self.nume = nume
        self.pret = pret
        self.stoc = stoc

    def __str__(self):
        f = f"\n -------------- " \
            f"\n{self.__class__.__name__} " \
            f"\n -------------- " \
            f"\n Nume = {self.nume} " \
            f"\n Pret = {self.pret} " \
            f"\n Stoc = {self.stoc}"
        return f


class Accesorii(Haine):

    def __init__(self, nume, pret, stoc, material, **kwargs):
        super().__init__(nume, pret, stoc, **kwargs)
        self.material = material

    def __str__(self):
        f = super().__str__()
        f += f"\n Material = {self.material}"
        return f


class Incaltaminte(Haine):
    def __init__(self, nume, pret, stoc, **kwargs):
        super(Incaltaminte, self).__init__(nume, pret, stoc)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        f = super().__str__()
        for attribute_ in dir(self):
            if '__' in attribute_ or attribute_ in ['name','pret','stoc']:
                continue
            f += f'\n {attribute_}={getattr(self, attribute_)}'
            return f

class Genti(Incaltaminte):
    pass

if __name__ == '__main__':
    bluze = Haine('T-shirt', 50, 25)
    bratara = Accesorii('Test', 100, 50, 'aur')
    print(bratara.material)
    print(bluze.nume)
    print(bluze.pret)
    print(bluze.stoc)
    pantofi = Incaltaminte('pantof', 50, 100, marime=40, material='piele', culoare='black')
    geanta = Genti('geanta', 50, 100, material='piele', culoare='black')
    print(pantofi.marime)

