class Animal:
    #double underscore is a special name for a class function which operates as an initializer
    #then the 'self' the object method
    #then the three different parameters 'type, name, and sound'
    def __init__(self, type, name, sound):
        #initializing the object variable
        self._type = type   #object variables have _ infront traditionally for better readability
        self._name = name
        self._sound = sound

    #getter functions==============
    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound
    #=============================

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

def main():
    #Creating an object "a0" and "a1"
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    #========================================
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronica', 'hello'))

if __name__ == '__main__': main()

#HENCE the sequence of creating the class
# 1. Declare a class
# 2. Declare default constructor and object of method
# 3. Define a getter functions
# 4. Call the functions by the object method or newly initialising the constructor