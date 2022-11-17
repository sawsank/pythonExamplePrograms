dict1 = { 1:'a', 2:'b'}
dict2 = { 2:'c',4:'d' }

print(dict1 | dict2)
#output skips the first 2 entity

dict1 = {1:'a',2:'b'}
dict2 = {2:'c',4:'d'}

print({**dict1, **dict2})
#output skips the first 2 entity

dict1 = {1:'a',2:'b'}
dict2 = {2:'c',4:'d'}

dict3 = dict2.copy()
dict3.update(dict1)

print(dict3)
#output skips the first 2 entity

