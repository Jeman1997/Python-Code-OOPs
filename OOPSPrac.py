class Emp:
    def __init__(self,fname,lname,pay):
        self.fn = fname
        self.ln = lname
        self.p  = pay
    def __str__(self):
        return self.fn
class Dev(Emp):
    pass
emp1=Dev('Jeman',"kumar",2000)
print(emp1)
print(emp1.__dict__)