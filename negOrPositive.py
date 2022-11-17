num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("zero")
else:
    print("negative number")

##using nested if
numm= float(input("enter a number:"))
if numm >= 0:
    if numm == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")