##Using ANSI escape sequences
print('\x1b[38;2;5;86;243m' + 'Programiz' + '\x1b[0m')
print('\033[38;2;48;5;57m' + 'Programiz' + '\x1b[0m')
print('\u001b[31;1m' + 'Programiz' + '\x1b[0m')
print('\033[31;44m' + 'Programiz' + '\x1b[0m')

##Using python module termcolor
from termcolor import colored

print(colored('Programiz', 'red'))