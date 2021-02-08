
class A:

    def __init__(self):
        print('in A init')

    def feature1(self):
        print('Feature 1 A is working')

    def feature2(self):
        print('Feature 2 A is working')


class B:

    def __init__(self, *args, **kwargs):
        print('in B init')

    def feature1(self):
        print('Feature 1 B is working')

    def feature2(self):
        print('Feature 2 B is working')


class C(A, B):
    def __init__(self, *args, **kwargs):
        # super recall the superclass to subclass
        super(C, self).__init__(*args, **kwargs)
        print('In C init')

    # accessing super class method using 'super()'
    def feature(self):
        super().feature2()
c1 = C()
c1.feature1()
c1.feature()
