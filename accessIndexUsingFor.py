my_list = [21, 44, 35,11]

for index, val in enumerate(my_list):
    print(index, val)
print()
#indexing with non zero value
my_list = [21,44,35,11]

for index, val in enumerate(my_list, start=1):
    print(index, val)
print()
#Without using enumerate()
my_list = [21, 44, 35, 11]

for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)
print()