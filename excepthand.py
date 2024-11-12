# import os
# try:
#     nameoffile =input("enter the name of file")
#     myfile=open(nameoffile,'r')
#     print(myfile.read())
#     myfile.close()
# except:
#     print("exception occured")
# finally:
#     print("execution completed")

try:
    x=int(input("enter number :"))
    y=input("enter text : ")
    print(x+y)
except TypeError:
    print("type error")


# try:
#     a=int(input("enter first number"))
#     b=int(input("enter second number"))
#     result=a/b
#     print("Result= ",result)
# except ZeroDivisionError:
#     print("zero division error")
# else:
#     print("execution sucessful")

