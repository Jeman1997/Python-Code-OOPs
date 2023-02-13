class Employee:
    raise_amnt=1.04
    def __init__(self,fname,lname,sal):
        self.fn = fname
        self.ln = lname
        self.sal= sal
    def __str__(self):
        return self.fn
    @classmethod
    def setraise(cls,amt):
        cls.raise_amnt=amt
class Emppp(Employee):
    pass

emp1=Emppp("Jeman","Kumar",20000)
print(emp1)
print(emp1.__dict__)
Employee.setraise(200000)
print(emp1.raise_amnt)
print(Employee.raise_amnt)