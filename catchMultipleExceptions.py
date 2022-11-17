string = input()


try:
    num = int(input())
    print(string + num)
except (TypeError, valueError) as e:
    print(e)