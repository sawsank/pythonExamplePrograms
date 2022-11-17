#Count Number of Digits in an Integer using while loop
num = 3452667
count = 0

while num != 0:
    num //= 10
    count +=1

print("Number of digits: " + str(count))

#Using inbuilt methods
num = 12345600000000
print(len(str(num)))