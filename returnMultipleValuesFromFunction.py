#Return values using comma
def name():
    return "john", "armin"

#print tuple with the returned values
print (name())

#get the individual items
name_1, name_2 =  name()
print(name_1, name_2)

#Using a dictionary
def name():
    n1 = "John"
    n2 = "Armin"

    return {1:n1, 2:n2}

names = name()
print(names)