#using yield
def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

chunk_size = 3
my_list = [1,2,3,4,5,6,7,8,9]
print(list(split(my_list, chunk_size)))

#the same thing using list compression
chunk_size = 2
list_chunked = [my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)]
print(list_chunked)
"""Using a for loop and range() method, 
iterate from 0 to the length of the list 
with the size of chunk as the step.
Return the chunks using yield.
 list_a[i:i+chunk_size] gives each chunk. 
 For example, when i = 0, the items included in 
 the chunk are i to i + chunk_size which is 0 to 
 (0 + 2)th index. In the next iteration, the items
  included are 2 to 2 + 2 = 4."""

#Using numpy
import numpy as np

my_list = [1,2,3,4,5,6,7,8,9]
print(np.array_split(my_list, 5))