class A:
    attr_A = 'A'
    custom = 'my_custom_text'

    def my_method(self):
        print(self.custom)


class B(A):
    attr_B = 'B'
    custom = 1


class D():
    attr_D = 'D'
    custom = 2


class C(D, B, A):
    attr_C = 'C'
    custom = 10

    def __init__(self):
        print('Custom attribute is: ', self.custom)
        print('Custom attr inherited: ', super(C, self).custom)



a = A()
b = B()
c = C()
d = D()
# print(b.attr_A)
# print(b.attr_B)
# print(c.custom)
c.my_method()