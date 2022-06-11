def main():
    f = open('lines.txt')
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()

# And there's a method here you may not have seen on the string, obviously each of the
# lines is returned as a string, and the string class has an R-strip method, which will strip any white space,
# including new lines, from the end of the line. And this allows us to print them or to do whatever with them 
# without having to worry about dealing with the line endings. A little bit about the open function here, by default, 
# it opens the file in read-only mode, which would be the same as providing a mode with a R letter. Open takes 
# an optional second argument, which if it's a simple letter R will open in read mode. If it's a W, it will open it in 
# write mode, and if you open in write mode, it empties the file if the file is not empty, and it starts at the beginning 
# and writes over the file. If the file doesn't exist, it creates it. A is a pen mode, this is just like write, 
# but if the file already has some content in it, it starts at the end of the file and it does not empty the file 
# and it does not create the file. There's an optional plus, which you can use with any of these modes, which will allow you 
# to both read and write. And there's an optional letter B or T, which will specify binary or text mode. And we'll look 
# at the meaning of binary and text mode later in this chapter, but it's worthwhile to know that it defaults in text mode.