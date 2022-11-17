def compute_hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = int(input("Enter largest positive integer: "))
num2 = int(input("Enter another not same largest positive integer: "))

print("The hcf is ", compute_hcf(num1, num2))

# Function to find HCF the Using Euclidian algorithm
def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(num1, num2)
print("The HCF is", hcf)