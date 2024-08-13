'''a1=int(input("enter lower number"))
a2=int(input("enter upper number"))

while(a1<=a2):
    if(a1%2==0):
        print(a1)
    a1=a1+1

#optimised way

if(a1%2==0):

    a1=a1
else:
    a1=a1+1

while(a1<=a2):
    print(a1,end=" ")
    a1=a1+2
print("\nend of code")'''

#prime number 
'''a1=int(input("enter the number"))

if(a1==0 or a1==1):
    print("it's not a prime number")
else:
    i=2
    k=0
    while(i<a1):
        if(a1%i==0):
            k=k+1
            break
        i=i+1
    if(k==0):
        print("prime")
    else:
        print("not prime")'''


#sum of digit
'''a1=int(input("enter the number"))
sum=0
while(a1>0):
    r=a1%10
    sum=sum+r
    a1=a1//10 
print(sum," is the sum")'''


#reverse of a number
'''a1=int(input("enter the number"))
new=0
while(a1>0):
    r=a1%10
    new=new*10+r
    a1=a1//10
print(new)'''

#factorial
'''a1=int(input("enter the number"))
fact=1
i=1
while(i<=a1):
    fact=fact*i
    i=i+1
print(fact)'''


#sumof neg and postive number
n=1
sump=0
sumn=0
while n!=0:
    n=int(input("enter your number"))
    if(n>0):
        sump=sump+n
    else:
        sumn=sumn+n
print(sump,"is sum of p number")
print(sumn, "is sum of neg number")


