import cmath

a = 1
b = 5
c = 6

##calculate the discrimant

d = (b**2) - (4*a*c)

soln1 = (-b-cmath.sqrt(d))/(2*a)
soln2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(soln1,soln2))

