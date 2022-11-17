#Using strip()
my_string = " Python "

print(my_string.strip())

my_string = " \n\n\nPython "

print(my_string.strip(" "))

##Using regular expression
import re

my_string  = " Hello Python "
output = re.sub(r'^\s+|\s+$', '', my_string)

print(output)