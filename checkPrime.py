num = 29

flag = False

if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not prime number")
else:
    print(num, " is a prime number")

num = 407

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num , "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(num, "is a prime number")
else:
    print(num,"is not a prime number")