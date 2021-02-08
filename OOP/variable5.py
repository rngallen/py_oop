'''
We have two type of variables
    > Instace variables
    >class (static) variables
'''


class Car:
    #property not attached to instance
    wheels = 4
    def __init__(self, *args, **kwargs):
        self.mil = 10
        self.com = 'BMW'
        self.cc = 1490
        super(Car, self).__init__(*args, **kwargs)


c1 = Car(); c2 = Car()
c1.mil = 2903329; c1.cc = 3500
#this will affect all  instances on Car class
Car.wheels = 5

print(c1.mil, c1.com, c1.cc, c1. wheels)
print(c2.mil, c2.com, c2.cc, c2.wheels)
