num1 = input('Enter first number: ')
num2 = input('Enter second number:')

sum = float(num1) + float(num2)

print('the sum of {0} and {1} is {2}'.format(num1, num2, sum))


#using single statement
print('the sum is %.1f' %(float(input('Enter first number:')) + float(input('Enter second number:'))))
