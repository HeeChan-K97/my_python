# print('Hello, World.')

x = 42
y = 73
print('the number is {} {}'.format(x, y))
print('the number is {xx} {bb}'.format(xx=x,bb=y))
print('the number is {bb} {xx}'.format(xx=x,bb=y))

print('the number is {0} {1}'.format(x, y))
print('the number is {0} {1} {0}'.format(x, y))

print('the number is {0:<5} {1:>5}'.format(x, y))
print('the number is {0:<5} {1:>05}'.format(x, y))

z = 33 * 571

print('the number is {:,}'.format(z))
print('the number is {:,}'.format(z).replace(',' '.'))#replacing comma by period
print('the number is {z:.f}')

#placeholder's importance
#triple quotes are used when the string has white spaces