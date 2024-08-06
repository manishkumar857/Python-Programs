'''x=int(input("enter a number"))
if(x<0):
    print("number is negative")
else:
    if(x%2==0 and x!=0):  
        print("number is even")
    elif(x==0):
        print("number is zero")
    else:
        print("number is odd")
print("program ended successfully")'''


'''x=int(input("enter 1st "))
y=int(input("enter 2nd "))
z=int(input("enter 3rd   "))

if(x>y and x>z):
    print("greatest number is ",x)
elif(y>x and y>z):
    print("greatest number is ",y)
else:
    print("greatest number is ",z)'''

#if will works for ALL non zero value

'''if(1):
    print("sucessfull")
else:
    print("unsucessfull")

if(8):
    print("sucessfull")
else:
    print("unsucessfull")

if(0):
    print("sucessfull")
else:
    print("unsucessfull")

x=None

if(x):
    print("sucess")
else:
    print("unsucessfull")'''

x = int(input("Enter 1st number:"))
y = int(input("Enter 2nd number:"))
z = int(input("Enter 3rd number:"))

'''if(x>y and x>z):
    print(x,"is greatest")
elif(y>x and y>z):
    print(y,"is greatest")
elif(z>y and z>y):
    print(z,"is greatest")
elif(x==y and y==z and z==x):
    print("all number are equal")
elif(x==y or y==z or z==x ):
    print("any two number are equal")'''

if((x>y and x<z) or (x>z and x<y)):
    print(x, "is the middle number")
 
elif((y>x and y<z) or (y>z and y<x)):
    print(y,"is middle number")

elif((z>y and z<x) or (z<y and z>x)):
    print(z,"is middle number")