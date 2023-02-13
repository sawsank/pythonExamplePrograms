'''class Vehicle:
    def __init__(self,driver,wheels,seats):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats

veh_1 = Vehicle("Sandy", 4, 2)
print(veh_1)

Output
 __main__.Vehicle object at 0x0000019ECCCA05F8'''

class Vehicle:
    def __init__(self,driver,wheels,seats):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats

    def __str__(self):
        return "Driver Name:" + self.driver + "" +"Number of seats in cab: " + str(self.noofseats)

veh_1 = Vehicle("Sandy", 4, 2)
print(veh_1)