class car:
    #attribute
    year = 2016
    mpg = 20
    speed = 100

    #methods
    def accelerate(self):
        return car.speed + 20

    def brake(self):
        return car.speed - 50

car1 = car()

print(car1.accelerate())
print(car1.brake())
print(car1.year)

print(car1.mpg)
print(car1.speed)