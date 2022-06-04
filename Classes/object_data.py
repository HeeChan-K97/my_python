class Animal:
    def __init__(self, **kwargs):#contructor
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'#these variables only exsist when the object is created from the class
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1)

    a0._name = 'Joe';#always a bad idea changing the private member
    print(a0._name)

if __name__ == '__main__': main()

##########################IMPORTANT###############################
#Variable is associated with the class and only exist in the class
#Object is drawing data from the class
#This characteristic is called encapsulation, 
# so if my data is encapsulated the data is belong to the object not to the class