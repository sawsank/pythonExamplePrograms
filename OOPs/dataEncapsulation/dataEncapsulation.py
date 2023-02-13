class Flat:
    def __init__(self):
        self.type = "premium"
        self.__bhk = "3 bhk"

flat_1 = Flat()
print(flat_1.type)

print(flat_1.__bhk)
'''
When we use two underscores '__' before attribute name, 
it makes attribute not accessible outside class. 
It becomes private attribute which means you can't read and write to those attributes except inside of the class. 
It is generally used by the developer of the module.
When you don't use underscore before attribute, 
it is a public attribute which can be accessed inside or outside of a class.'''