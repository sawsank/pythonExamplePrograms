class Company:

    name = "XYZ Bank"
    turnover = 5000
    revenue = 1000
    no_of_employees = 100

    def productivity(self):
        return Company.revenue/Company.no_of_employees

##Attributes which are defined outside of method can be extracted without creating object.

print(Company.name)

print(Company.turnover)

print(Company.no_of_employees)

print(Company.revenue)

print(Company().productivity())