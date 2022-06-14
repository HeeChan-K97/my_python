# print('Hello, World.')

class bunny:
    def __init__(self,n):
        self._n = n
    def __repr__(self):
        return f'repr: the number is {self._n}'
    def __str__(self):
        return f'str: the number is {self._n}'

        #this would help to customise how it's going to be represented in different contexts

x = bunny(47)
print(x)# this will default to str version
print(ascii(x))# represents only the ascii characters
print(chr(128406))#chracter of a number
print(ord('🖖'))#gives the num of character

# print(repr(s))#repr = representation, repr will print the value returned


