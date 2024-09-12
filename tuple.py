CAmarks = (10,20,30,25,19,20) #tuple is ordered and is unchangeable and allow duplicates
print(CAmarks)
print(type(CAmarks))

print(CAmarks[-1])
print(CAmarks[0:3])
print(CAmarks[-3:])

idx=int(input("enter the index : "))
inp = int(input("enter the element : "))
# CAmarks[idx] = inp
# print(CAmarks) #this will not work as tuples are unchangeable 
