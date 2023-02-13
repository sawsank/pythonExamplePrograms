class Cab:
     #Initialise variables for first iteration
    numberofCabs = 0
    numPassengers = 0

    def __init__(self,driver,kms,places,pay,passengers):
        self.driver = driver
        self.running = kms
        self.places = places
        self.bill = pay
        Cab.numberofCabs = Cab.numberofCabs + 1
        Cab.numpassengers = Cab.numPassengers + passengers

    #Returns price of cab fare per km
     #instance method
    def rateperkm(self):
        return self.bill/self.running

    #Returns number of cabs running
    @classmethod
    def noofcabs(cls):
         return int(cls.numPassengers/cls.numberofCabs)

    #returns average number of passengers travelling in a cab
    @classmethod
    def avgnoofpassengers(cls):
         return int(cls.numPassengers/cls.numberofCabs)

    @staticmethod
    def billvalidation(pay):
         return int(pay) > 0

firstcab = Cab("Ramesh", 80,['Delhi','Noida'],2200,3)
secondcab = Cab("Dave",20,['Gurgaon','Noida'], 1500, 1)
thirdcab =Cab("Dave",20,['Gurgon','noida'],680,2)

print(firstcab.driver)
print(secondcab.driver)
print(thirdcab.driver)

print(firstcab.rateperkm())

print(secondcab.rateperkm())

print(thirdcab.rateperkm())

print(Cab.noofcabs())

print(Cab.avgnoofpassengers())



print(Cab.billvalidation(0.2))