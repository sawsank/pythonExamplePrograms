class MyCompany:

    def __init__(self,compname,revenue,employeesize):
        self.name= compname
        self.revenue = revenue
        self.no_of_employees = employeesize

    def productivity(self):
        return self.revenue/self.no_of_employees

print(MyCompany('XYZ Bank', 1000,100).productivity())

#Alternative way of calling the class method
Bank = MyCompany('ABC Bank', 5000,200)
print(MyCompany.productivity(Bank))