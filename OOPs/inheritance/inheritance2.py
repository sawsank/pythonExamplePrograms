class Vehicle:
    minimumrate = 50
    def __init__(self,driver,wheels,seats):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats

class Cab(Vehicle):
    minimumrate = 75


print(Vehicle.minimumrate)
print(Cab.minimumrate)