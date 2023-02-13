##update first and last name automatically by changing email address
class Vehicle:
    def __init__(self,driver_firstname, driver_lastname):
        self.fdriver = driver_firstname
        self.ldriver = driver_lastname

    @property
    def email(self):
        return self.fdriver+ '.' + self.ldriver+'@uber.com'

    @email.setter
    def email(self,address):
        first = address[:address.find('.')]
        last = address[address.find('.')+1:address.find('@')]
        self.fdriver = first
        self.ldriver = last

veh_1 = Vehicle("Sandy", "Stewart")
veh_1.email = 'deep.bhalla@uber.com'
print(veh_1.fdriver)

print(veh_1.ldriver)