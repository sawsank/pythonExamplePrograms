#Access both key and value using items()
dt = {'a': 'juice', 'b':'grill','c':'corn'}

for key, value in dt.items():
    print(key, value)

#Access both key and value without using items()
for key in dt:
    print(key, dt[key])
    print()

#Access both key and value using iteritems()
"""for key, value in dt.iteritems():
    print(key, value)
    print()
    #iteritems library only available for python 2
"""
#Return keys or values explicitly
for key in dt.keys():
    print(key)
for value in dt.values():
    print(value)
    print()