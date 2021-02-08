class Computer:

    def __init__(self, *args, **kwargs):
        self.name = "Luqman"
        self.age = 53
        super(Computer, self).__init__(*args, **kwargs)

    def compare(self, other, *args, **kwargs):
        if self.age == other.age:
            return True



# createing objects
c1 = Computer()
c1.name = 'Kikwete'
c1.age = 98
c2 = Computer()

print(c1.name)
print(c2.name)

if c1.compare(c2):
    print('They are the same')
else:
    print('They are Different')
