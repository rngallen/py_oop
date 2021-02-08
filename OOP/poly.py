

'''
PLOYMORPHISM

POLY => MANY
MORPH => FORM
ISM =>


4 ways in implementing polymorphism
i.      Duck Typing
ii.     Operator Overloading
iii.    Method Overloading
iv.     Method Overriding
'''
#Duck Typing

class VsCode:
    def execute(self):
        print('Compiling...')
        print('Running....')


class MyEditor:
    def execute(self):
        print('Spell Check...')
        print('Convention Check...')
        print('Compiling....')
        print('Running...')

class Laptop:
    def code(self, ide, *args, **kwargs):
        ide.execute()


a = MyEditor()
lap1 = Laptop()
lap1.code(ide=a)