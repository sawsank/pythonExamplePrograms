import itertools

my_list = [[1],[2,3],[4,5,6,7]]

flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)

#Using Nested for Loops (non pythonic way)
my_lst =[[1],[2,3],[4,5,6,7]]

flat_list = []
for sublist in my_lst:
    for num in sublist:
        flat_list.append(num)

print(flat_list)

#Using itertools package
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = list(itertools.chain(*my_list))
print(flat_list)

#Using sum()
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = sum(my_list, [])
print(flat_list)

#Using lambda and reduce()
from functools import reduce

my_list = [[1], [2, 3], [4, 5, 6, 7]]
print(reduce(lambda x, y: x+y, my_list))
