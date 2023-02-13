class Employee:
    raise_amt=1.04
    def __init__(self,firstn,lastn,pay):
        self.fn=firstn
        self.ln=lastn
        self.p =pay
    def applyraise(self):
        self.p=self.p*self.raise_amt
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amt=amount
emp1=Employee('jeman','kumar',1000)
emp2=Employee('jeevan','kumar',3000)

Employee.set_raise_amount(1.05)

#print(Employee.raise_amt)
#print(emp1.raise_amt)
#print(emp1.raise_amt)

class Employee2:
    raise_amt=1.04
    def __init__(self,firstn,lastn,pay):
        self.fn=firstn
        self.ln=lastn
        self.p =pay
    def applyraise(self):
        self.p=self.p*self.raise_amt
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amt=amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)
        

emp21='Jeman-Kumar-2000'
emp22='Jeevan-Kumar-2000'
emp21=Employee2.from_string(emp21)
#print(emp21.__dict__)
emp22=Employee2.from_string(emp22)
#print(emp22.__dict__)


class Employee:
    raise_amt=1.04
    def __init__(self,firstn,lastn,pay):
        self.fn=firstn
        self.ln=lastn
        self.p =pay
    def applyraise(self):
        self.p=self.p*self.raise_amt
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amt=amount
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

import datetime
mydate=datetime.date(2016,7,10)
print(Employee.is_workday(mydate))
            
