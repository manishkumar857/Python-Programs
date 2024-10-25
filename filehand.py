#how to check file is there or not
import os
filename = input("Enter your file name: ") #in input have to give file location
if os.path.exists(filename):
    myfile = open(filename,"r")
    print(myfile.read())
    myfile.close()
else:
    print("file doesn't exist:" )

#how to check file is there or not if there print only some number of char
import os
filename = input("Enter your file name: ") #in input have to give file location
num = int(input("Enter how mnay character you wants to print: "))
if os.path.exists(filename):
    myfile = open(filename,"r")
    print(myfile.read(num))
    myfile.close()
else:
    print("file doesn't exist:" )

import os
filename = input("Enter your file name: ") #in input have to give file location
if os.path.exists(filename):
    myfile = open(filename,"r")
    print(myfile.readline(1000))
    myfile.close()
else:
    print("file doesn't exist:" )