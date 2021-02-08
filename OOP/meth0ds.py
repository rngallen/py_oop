import datetime

'''
Generally we have 3 types of methods
    >Instance method
    >Class methods
    >Static methods
'''


class Student:
    # class/static variable
    school = 'Tanga Technical School'

    def __init__(self, m1, m2, m3, *args, **kwargs):
        # instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        super(Student, self).__init__(*args, **kwargs)

    # instance method
    def avg(self):
        total = self.m1 + self.m2 + self.m3
        average = total/3
        return average

    # accessor method > for accessing/fetching
    def get_m1(self):
        return self.m1

    # mutator method > for changing/mutate
    def set_m1(self, value):
        self.m1 = value

    # class method
    @classmethod
    def school_info(cls):
        cls.school = 'Moshi Tech'
        return cls.school

    # static method neither relating to class nor instance
    @staticmethod
    def info():
        now = datetime.datetime.now()
        return now.strftime('%c')


s1 = Student(88, 98, 90)
s2 = Student(89, 92, 83)


print(s2.avg())
print(s2.get_m1())
s2.set_m1(32)
print(s2.avg())
print(s2.get_m1())


print(Student.school_info())
print(Student.info())


