class Duck:
    #Data========Object=============
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'
    #===============================
    def quack(self):#self is an argument which is the reference to the object, not the class but to the object
        print(self.sound)#so when an object is created, the self can dereference the initialised member

    def move(self):
        print(self.movement)

def main():
    donald = Duck()
    donald.quack()
    donald.move()

if __name__ == '__main__': main()# this is how we call main func in py