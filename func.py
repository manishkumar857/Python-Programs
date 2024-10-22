# def first():
#     print("hello world")


# first()

# x=input("enter name")
# def firstp(x):
#     print("name is ",x)


# firstp(x) 


# def input1():
#     y=int(input("number 1"))
#     y2=int(input("number 2"))
#     process(y,y2)

# def process(y3,yy4):
#     print(y3+yy4)

# input1()

# def fun(*vals):
#     sm=0
#     for i in vals:
#         temp=i.split(",")
#         for x in temp:
#             sm=sm+x
#     print(sm)
#     print(vals,type(vals))
    
# nums = input("enter number")
# temp=nums.split(",")
# print(temp)

# fun(temp)


# def proce(num1=12):
#     print("you entered {}.".format(num1))

# proce(14)

# def inp(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact+1
#         print("factorial of {} is {}".format(num,fact))

# num=int(input("enter no "))
# inp(num)

# def inp1(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i

    
# num=int(input("enter no "))
# inp1(num)
# print("factorial of {} is {}".format(num,inp1(num)))

def inp2(num2):
    if(num2==1 or num2==0):
        return 1
    else:
        num2*inp2(num2-1)
num2=int(input("enter no"))
