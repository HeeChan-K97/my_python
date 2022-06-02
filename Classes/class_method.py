class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t = None):   #this way of defining a functions works as either setter and getter.
        if t: self._type = t    #when there is a value to return it will set by itself before retunring it but else return value of type
        return self._type       #object variable has _ , indicates it is private variable

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):#definition of function self
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    #a0.sound('bark')
    print(a0)
    print(a1)

if __name__ == '__main__': main()