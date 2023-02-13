class Message:
    def details(self, phrase = None):
        if phrase is not None:
            print('My message -' + phrase)
        else:
            print('Welcome to Python World!')

x = Message()

print(x.details())

print(x.details("Life is Beautiful"))