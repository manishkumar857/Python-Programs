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


with open("Data.txt","r") as f:
    print(f.read())

with open("Data.txt","w") as f:
    f.write("new data")

import os
os.remove("sample.txt")