# sorting a list
class MyObj():
    attr1 = 'a'

    def __init__(self, value):
        self.attr1 = value

    def __lt__(self, other):
        if self.attr1 < other.attr1:
            return True
        return False

    def __str__(self):
        return str(self.attr1)

    def __repr__(self):
        return str(self.attr1)


obj1 = MyObj(5)
obj2 = MyObj(7)
obj3 = MyObj(3)

a = [obj1, obj2, obj3]
print(a)
a.sort()
print(a)
