#Using random module
import random

my_list = [1, 'a', 32, 'c', 'd', 31]
print(random.choice(my_list))

#Using secrets module
import secrets

my_list = [1, 'a', 32, 'c', 'd', 31]
print(secrets.choice(my_list))