a1=int(input("enter lower number"))
a2=int(input("enter upper number"))

'''while(a1<=a2):
    if(a1%2==0):
        print(a1)
    a1=a1+1'''

#optimised way

if(a1%2==0):

    a1=a1
else:
    a1=a1+1

while(a1<=a2):
    print(a1,end=" ")
    a1=a1+2
print("\nend of code")

