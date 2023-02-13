#__init__ method to construct a class
#access class dir with __dict__ method
#create objects with class
#class variables/attributes
#class methods
#Static Methods
#Inheritance
#Special Methods
class Employee:
    raise_amt=1.04
    def __init__(self,fname,lname,pay):
        self.first=fname
        self.lname=lname
        self.pay  =pay
    def __repr__(self):
        return self.first+' '+self.lname+' object'
    def __str__(self):
        return self.first+' '+self.lname+' object'
    def __add__(self,other):
        return self.pay+other.pay
print(Employee)
emp1=Employee('Jeman','Kumar',23)
emp2=Employee('Jeevan','Kumar',24)
print(emp1+emp2)
print(emp1)