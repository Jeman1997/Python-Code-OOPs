class Emp:
    rais_amt=1.04
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.pay  =pay
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)
    def apply_raise(self):
        self.pay=self.pay*rais_amt
    
class Developer(Emp):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
class Manager(Emp):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(frist,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    
    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())
emp1=Emp('Jeman','Kumar',1000)
emp2=Developer('Jeevan','Kumar',2000,'C++')
print(emp1.__dict__)
print(emp2.__dict__)