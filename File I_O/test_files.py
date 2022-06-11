def main():
    infile = open('lines.txt', 'rt')#open the text file in read mode and text mode
    outfile = open('lines-copy.txt', 'wt')#since we dont have this file the python will open the file as a write mode
    for line in infile:#read each lines of the 'lines.txt'
        print(line.rstrip(), file=outfile)#print the lines and use rstrip method
        # outfile.writelines(line)
        print('.', end='', flush=True)#flushes the output buffer. 
                                      #On some operating systems, the output buffer is flushed, and you may not get any of those dots printed until you print a new line,
    outfile.close()# to prevent any data leak, this is a good habit for the data
    print('\ndone.')

if __name__ == '__main__': main()


#explicit is always better than implicit

# RESULT
# as a result, we can find we have create a file called "lines-copy.txt" 
#===================================================================================================================
# print(line.rstrip(), file=outfile)
# outfile.writelines(line)

    # : The difference is is that with the print function, I'm able to strip these line endings, 
    #   and rewrite the line endings with the default line endings for this operating system, which print does by 
    #   default, and that way, if my input file is from another operating system with different line endings, I'm 
    #   actually serving to translate those line endings into the correct one for this operating system, 
    #   so it's important to know that distinction.