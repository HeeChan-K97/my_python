class RevStr(str):#inheriting the str which is not capitalised. Which means it is built-in class provided by python3
    def __str__(self):
        return self[::-1]#print backwards

def main():
    hello = RevStr('Hello, World.')
    print(hello)

if __name__ == '__main__': main()

#RESULT

#.dlroW ,olleH