class Vehicle:
    minimumrate = 50
    def __init__(self,driver,wheels,seats,kms,bill):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats
        self.running = kms
        self.bill = bill

    def rateperkm(self):
        return self.bill/self.running

class Cab(Vehicle):
    minimumrate = 75
    def __init__(self,driver,wheels,seats,kms,bill,cabtype):
        Vehicle.__init__(self,driver,wheels,seats,kms,bill)
        self.category = cabtype

class Bus(Vehicle):
    minimumrate = 25
    def __init__(self,driver,wheels,seats,kms,bill,color):
        Vehicle.__init__(self,driver,wheels,seats,kms,bill)
        self.color = color

cab1 = Cab('Prateek',4,3,50,700,'SUV')
print(cab1.category)
print(cab1.rateperkm())

bus1 = Bus('Dave',4,10,50,400,'green')
print(bus1.color)
print(bus1.rateperkm())