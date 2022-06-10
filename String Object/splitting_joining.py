from posixpath import split


s = 'THIS is a long string with a bunch of words in it.'
l = s.split()
s2 = ' == '.join(l)
print(s.split('i'))#can specify a word 
print(s2)
print(s.title())