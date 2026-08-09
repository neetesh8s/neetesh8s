
class A:

    def __init__(self):
        print('init in A')

    def f1(self):
        print('f1 show')

class B(A):

    def __init__(self):

        print('init in B')
        super().__init__()
        
    def f2(self):
        print('f2 show')
        super().f1()



obj1 = B()
obj1.f2()