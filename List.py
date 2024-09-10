# ls = [2,2,4,5,5,6] # list are mutable , it allows duplicates values , can contain d/f datatypes
# print(ls)

# ls.append(2) #can add only one argument
# print(ls)
# ls.append(2)

# ls2=[3,3,3,3,3,3]
# ls.extend(ls2)
# print(ls)

# ls.insert(0,76) #index,value
# print(ls)

#slicing in list
# ls=[6,7,8,9,3]
# print(ls[0])
# print(ls[::1])#[start:end:stride(space in between])
# print(ls[1::1])
# print(ls[::2])
# print(ls[::-1])

# print(ls)
# print(ls.pop(0)) #   pop() remove last element ,pop(inex value) remove index value
# print(ls)

# print(ls.remove(9)) # element name in ()
# print(ls)

# del ls[0:3]
# print(ls)


n =int(input("enter the no of elements till you want to print"))
i=0
x=0
ls1 =[]
while(x<=n):
    
    ls1.append(x)
    i=i+1
    x=i**3   
print(ls1)

