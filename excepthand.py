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

# try:
#     x=int(input("enter number :"))
#     y=input("enter text : ")
#     print(x+y)
# except (TypeError,ValueError):
#     print("error")
# finally:
#     print("end of code")

# try:
#     a=int(input("enter first number"))
#     b=int(input("enter second number"))
#     result=a/b
#     print("Result= ",result)
# except ZeroDivisionError:
#     print("zero division error")
# else:
#     print("execution sucessful")




#user defined exception handling
# class Error(Exception):
#     pass
# class ValueTooSmallError(Error):
#     pass
# class ValueTooLargeError(Error):
#     pass



# number=10
# while True:
#     try:
#         i_num=int(input("enter the number"))
#         if i_num<number:
#             raise ValueTooSmallError
#         elif i_num>number:
#             raise ValueTooLargeError
#         break
#     except ValueTooSmallError:
#         print("value too small")
#     except ValueTooLargeError:
#         print("values too large")
# print("you guessed it correctly")




class Error(Exception):
    pass
class NegativeNumber(Error):
    pass



while True:
    try:
        number=int(input("enter the number"))
        
        if number<0:
            raise NegativeNumber
    
            break
        elif number>0:
            break
    except NegativeNumber:
        print("value is negative")
        
    
print("value is positive")