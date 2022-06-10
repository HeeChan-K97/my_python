
print('Hello, World.')#we have methods like swapcase, upper, casefold... etc
#string is immutable 


s1 = 'Hello, World.'
s2 = s1.upper()
s3 = 'This is a new string'

print(id(s1))
print(id(s2))

print(s1 + s3)
print(s1 + ' ' + s3)#give space in between
#we can see that two objects are entirely different.
#which means the upper method is not just transforming the string but also creating a new object


