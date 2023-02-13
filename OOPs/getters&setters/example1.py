class Vehicle:
    def __init__(self,driver_firstname,driver_lastname):
        self.fdriver = driver_firstname
        self.ldriver = driver_lastname
        self.email  = self.fdriver + '.' + self.ldriver + '@uber.com'

veh_1 = Vehicle("Sandy", "Stewart")

print(veh_1.fdriver)
#Sandy

print(veh_1.email)
#'Sandy.Stewart@uber.com'

veh_1.fdriver = 'Tom'
print(veh_1.fdriver)
print(veh_1.email)
#'Tom'
