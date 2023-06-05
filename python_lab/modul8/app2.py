# create iterator that returns all it's attributes
class MyIter():

    def __init__(self):
        self.attr = dir(self)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.attr:
            raise StopIteration
        return self.attr.pop(0)

for attr in MyIter():
    print(attr)


