def main():
    infile = open('berlin.jpg', 'rb')# image file cannot be opened using text mode for eg) rt = read and text mode
    outfile = open('berlin-copy.jpg', 'wb')
    while True:#loop run until it is told to break 
        buf = infile.read(10240)#10kBytes, this is just the size of the chunks that you're reading and writing at a time, 
                                #it's not a limit of how big the file can be. Rather it's just a nice 
                                #limit of how much memory you're going to use while copying the file, one chunk at a time.
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()

# CODE EXPLANATION
# : Then we test if there is data in the buffer and of course an empty buffer is going to have a 
#   false comparative value and anything that's not empty is going to be true and then we write the buffer. 
#   It's as simple as that outfile.write with the buffer and then we print our little dot and if the buffer 
#   is empty we call break. So it's as simple as that and that breaks us out of the loop, we close the file.
#   Again we're closing the file to flush any buffers and make sure that the file is written properly and we print a new line and done.