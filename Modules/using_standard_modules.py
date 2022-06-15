#the python standard library: docs.python.org, refer to chapter 6, sys module
import sys
import os
# import datetime

def main():
    v = sys.version_info#version_info: returns a collection of information
    v = sys.platform
    v = os.name
    v = os.getenv('PATH')
    print('Python version {}.{}.{}'.format(*v))

if __name__ == '__main__': main()
