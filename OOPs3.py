class Emp:
    raise_amt=1.04
    def __init__(self,fname,lname,pay):
        self.fname= fname
        self.lname= lname
        self.pay  = pay
    def amt_raise(self):
        self.pay  = self.pay * self.raise_amt
