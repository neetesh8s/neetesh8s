


class A:

    def f1(self):
        print('f1 show')

    def f2(self):
        print('f2 show')

    def show(self):
        print('A show')

class B:
    def f3(self):
        print('f3 show')

    def f4(self):
        print('f4 show')

    def show(self):
        print('B show')
class C(A,B):
    def f5(self):
        print('f5 show')

    # def show(self):
    #     print('C show')
# first it will call show from C class but if not present then
# It will call look in A class based on order (A,B) 
# It will call look in B class if order is (B, A)  

obj1 = C()
obj1.show()