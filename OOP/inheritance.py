
# Single Level Inheritance
class A:
    # super class
    def feature1(self):
        print('Feature 1 working')

    def feature2(self):
        print('Feature 2 is working')


class B(A):
    # sub class
    def feature3(self):
        print('Feature 3 is working')

    def feature4(self):
        print('Feature 4 is working')


class C:
    # multi level inheritance
    def feature5(self):
        print('Feature 5 is working')


class D(A, C):
    pass
    # def feature6(self):
    #     print('Feature 6 is working')


a1 = A()
b1 = B()
d1 = D()


b1.feature4()
d1.feature1()

