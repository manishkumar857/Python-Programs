'''x=int(input("enter input"))

sum=0  
for i in range(1,x+1):
    cube=i**3
    sum=sum+cube

print(sum)'''

'''x=int(input("enter the last number"))
for i in range(1,x+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print(" ")'''

'''x=int(input("enter the last number"))
n=0
for i in range(1,x+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print(" ")'''



#sum of square of even number 
x=int(input("enter input"))

sum=0  
for i in range(1,x+1):
    if(i%2==0):
        sq=i**2
        sum=sum+sq
print(sum)