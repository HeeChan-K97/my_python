class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        self._start = 0
        self._step = 1
        
        if numargs < 1:
            raise TypeError(f'expected at least 1 argument, got {numargs}')
        elif numargs == 1:
            self._stop = args[0]
        elif numargs == 2:
            (self._start, self._stop) = args
        elif numargs == 3:
            (self._start, self._stop, self._step) = args
        else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

        self._next = self._start
    
    def __iter__(self):#making the object as iterator = __iter__
        return self

    def __next__(self):#which is the iteration itself, a construct like the for loop is going to look for this __next__ 
                      #function in order to treat this as an iterator, and in order to use it for iteration.
        if self._next > self._stop:
            raise StopIteration #stop the execution in an iterator class
        else:
            _r = self._next
            self._next += self._step
            return _r

def main():#Check the difference of the result affected by the iterator
    for n in inclusive_range(25):# Result:0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 
    #for n in inclusive_range(5, 25): #Result: 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 
    #for n in inclusive_range(5, 25, 5): #Result: 5 10 15 20 25 
        print(n, end=' ')
    print()

if __name__ == '__main__': main()

#raise StopIteration = stop the execution in an iterator class