import sys

def main():
    #print('Hello, World.')
    try:
        x = int('foo')
    except ValueError:
        print('Walala I gotchu')
#using the try and except(exception method) we can increase the readability of the code by letting readers know where the error might come from
#exceptions can be recognised on the terminal when the file executes for the above case it said "valueError" that is why I have put the except valueError:
# we can try with other types of exceptions
#FOR EXAMPLE
    try:
        x = 5/0
    # except ZeroDivisionError:
    #     print('That is ZeroDivisionError')
    except:
        print(f'unknow Error: {sys.exc_info()[1]}')

#However we can create an exception without specifying the excpetion error type        
# using <import sys> to give the error information when there is unexpected error in the program
if __name__ == '__main__': main()
