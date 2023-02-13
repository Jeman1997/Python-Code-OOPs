class Employee:
    def __init__(self,fname,lname,pay):
        self.fn=fname
        self.ln=lname
        self.p =pay
    
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.fn,self.ln)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.fn,self.ln)
    
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        self.fn=first
        self.ln=last
    
    @fullname.deleter #for this to delete use 'del emp1.fullname'
    def fullname(self):
        print("Deleted Name!")
        self.fn=None
        self.ln=None
        
emp_1=Employee('Jeman','Kumar',2000)