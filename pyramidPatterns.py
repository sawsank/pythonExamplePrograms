rows= int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end=" ")
    print("\n")

#print half pyramid a using numbers
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")

#print half pyramid using alphabets
rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i + 1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")

    ascii_value += 1
    print("\n")

#print inverted half pyramid using * and numbers
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")

    print("\n")

#Inverted half pyramid using numbers
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")

    print("\n")

#print full pyramid using *
rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end=" ")

    while k!=(2*i-1):
        print("*", end="")
        k +=1

    k = 0
    print()

#Full Pyramid of Numbers
rows = int(input("Enter number of rows: "))

k = 0
count = 0
count1 = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print("  ", end="")
        count += 1

    while k != ((2 * i) - 1):
        if count <= rows - 1:
            print(i + k, end=" ")
            count += 1
        else:
            count1 += 1
            print(i + k - (2 * count1), end=" ")
        k += 1

    count1 = count = k = 0
    print()

#Inverted full pyramid of *
rows = int(input("Enter number of rows: "))

for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()

#Pascal's Triangle
rows = int(input("Enter number of rows: "))
coef = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()

#Floyd's Triangle
rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()