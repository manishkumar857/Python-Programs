
'''#by default input is string type so we need to specify about the int type

a = int(input("enter first number"))
b = int(input("enter second number"))
print("sum ",a+b)'''

"""name = input("enter name ")
age = int(input("enter age "))
cgpa = float(input("enter cgpa "))
print("name:",name," age:",age," cgpa:",cgpa)"""

'''length = int(input("enter length "))
breadth =int(input("enter breadth "))  
print("area is",length*breadth)
b = length+breadth 
print("perimeter is",2*b)'''

'''tempINc = int(input("Enter temp in C ")) 
F = (9/5)*tempINc+32
print("Temp in farenheit is ",F,end=' ') 
print("for temp in C ",tempINc)
#end =' ' is used for removing next line 

print("Temp in farenheit is ",F,end='@')
print("for temp in C ",tempINc)

print("twinkle twinkle little star\n\thow i wonder what you are\n\t\tup above the world so high\nlike a diamond in the sky")'''



'''bill = int(input("enter amount "))

if(bill>1000):
    discount=bill/10
    bill = bill-discount
    print("final bill amount is ",bill," with a discount of ",discount)
else:
    print("final bill is ",bill)'''

num =100
num2='100'
num3=100.9
print(type(num))
print(type(num2))
print(type(num3))

n1,n2,n3 =100,200,300
print(n1,n2,n3)

n1=n2=n3 =100
print(n1,n2,n3) 

n4=9j
n5=True
n6=1
print(type(n4))
print(type(n5))
print(type(n6))