# f=open("hello.txt",'r')
# print(f)
# print(f.name)
# print(f.readable())
# #print(f.read())
# #print(f.readline())
# print(f.readlines())
# print(f.mode)
# f.close()
# print(f.closed)

# f=open("hello.txt",'w')
# f.write("this is new line")
# f=open("hello.txt",'r')
# data=f.readlines()

# print(data)
# for line in data:
#     print(line)


# f.close()

# f=open("Data.txt",'w')
# lst=["phy\n","chem\n","maths\n","computerscience\n"]
# f.writelines(lst)
# print("data entered sucessfully")
# f.close()


# with open("data.txt",'w') as f:
#     lst=["phy\n","chem\n","maths\n","computerscience\n"]
#     f.writelines(lst)
#     print(f.closed)
# print(f.closed)

# f=open("hello.txt",'a')
# f.write("this is new line")
# f.write("thisis appended line")
# f=open("hello.txt",'r')
# data=f.readlines()

# print(data)
# for line in data:
#     print(line)


#how to check file is there or not if not there create a new file and take input and print
#import os

# filename = input("Enter your file name: ") #in input have to give file location
# if os.path.exists(filename):
#     myfile = open(filename,"r")
#     num = int(input("Enter how many character you wants to print: "))
#     print(myfile.read(num))
#     myfile.close()
# else:
#     print("file doesn't exist:" )
#     res = input("do you want to create a new file (Y/N) ?").lower()
#     if res == "y":
#         myfile = open(filename,"w")
#         num = input("Enter how many character you wants to print: ")
#         myfile.write(num)
#         myfile.close()
#     else:
#         print("you can quit!")


#how to delete a file
#nameoffile=input("enter file name you want to delete : ")
# if os.path.exists(nameoffile):
#     os.remove(nameoffile)
# else:
#     print("file doesn't exist ")

# #how to rename a file
# if os.path.exists(nameoffile):
#     oldname=input("enter the old name here: ")
#     os.rename(nameoffile,oldname)
#     print("file name changed!")
# else:
#     print("file does not exist!")

# if os.path.exists(nameoffile):
#     myfile=open(nameoffile,"r")
#     print("current location: ",myfile.tell())
#     print(myfile.read())

#     print(myfile.seek(5))
#     print("current location: ",myfile.tell())
#     print(myfile.read())
#     myfile.close()
# else:
#     print("file does not exist!")



import csv
students=[
    {"John",85},
    {"Jane",92},
    {"Tom",75}

]

with open('hello.csv',mode='w',newline='')as file:
    writer = csv.writer(file)
    writer.writerow(students)

print("Multiple pairs of arguments written to csv successfully")
file.close()

