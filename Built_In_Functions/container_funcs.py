from re import X


x = ( 1 , 2 , 3 , 4 , 5 )
y=x
y=reversed(x)
for i in y: print(i)

y=list(reversed(x))

y=sum(x, 10)# 10 is the starting point, since the summation start with adding 10

y=max(x)
y=min(x)

y=any(x)#boolean function where checks the values and other than 0 is true
y=all(x)#boolean function checks if the values are all true 

print(x)
print(y)


a = (1,2,3,4,5)
b = (6,7,8,9,10)

z =zip(a,b)

for a, b in z: print(f'{a} == {b}')


c =('cat', 'dog', 'rabbit', 'eagle')
for i, v in enumerate(c, 1): print(f'{i}: {v}')# 1 is to give a starting point