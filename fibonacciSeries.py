iterms = int(input("Enter how many terms: "))

n1, n2 = 0, 1
count = 0

if iterms <=0:
    print("please enter a positive integer")
elif iterms == 1:
    print("Fibonacci sequence upto", iterms, ":")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while count < iterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1