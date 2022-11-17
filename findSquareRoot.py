#for positive numbers

num = 8

num_sqrt = num ** 0.5
print('the square root of %0.3f is %0.3f' %(num, num_sqrt))

## for real or complex numbers

import cmath

num= 1 + 2j

# To take input from the user
#num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('the square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))