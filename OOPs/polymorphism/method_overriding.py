class Vehicle:
    def message(self):
        print("Parent method!")

class Cab(Vehicle):
    def message(self):
        print("Child class method")

class Bus(Vehicle):
    def message(self):
        print("child Bus class method")

x= Vehicle()
print(x.message())

y = Cab()
print(y.message())

z= Bus()
print(z.message())