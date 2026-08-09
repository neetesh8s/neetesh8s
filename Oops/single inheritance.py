
class A:

    def f1(self):
        print('f1 show')

    def f2(self):
        print('f2 show')

class B(A):
    def f3(self):
        print('f3 show')

    def f4(self):
        print('f4 show')

obj1 = B()
obj1.f1