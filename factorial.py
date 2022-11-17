#Factorial of a Number using Loop

num = 7

factorial = 1

if  num <0:
    print("Sorry, factorial does not exist for negetive numbers")
elif num ==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

#Factorial of a Number using Recursion
def factorial(x):

    if x ==1:
        return 1
    else:
        return(x * factorial(x-1))

num = int(input("Enter a number: "))

result = factorial(num)
print("the factorial of", num, "is ", result)