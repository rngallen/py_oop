
class Student:

    def __init__(self, name, rollno, *args, **kwargs):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
        super(Student, self).__init__(*args, **kwargs)

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8
            
        def show(self):
            print(self.brand, self.cpu, self.ram)
        


s1 = Student('Luqman', 23)
s2 = Student('Chiluba', 1)
# print(s1.name, s1.rollno)
# print(s2.name, s2.rollno)

s2.show()
# a = s2.lap.brand
# print(a)
