CAmarks = (10,20,30,25,19,20) #tuple is ordered and is unchangeable and allow duplicates
print(CAmarks)
print(type(CAmarks))

print(CAmarks[-1])
print(CAmarks[0:3])
print(CAmarks[-3:])

midtmarks = (9,9,8,7,3,1,8)
finalmarks = CAmarks + midtmarks #concatenate
print(finalmarks)

print(finalmarks[::-1])
print(finalmarks[1:])
print(finalmarks[3:7])


#unpacking in tuple
tuplex = (2,2,5)
a,b,c=tuplex
print(c)

print(tuplex.count(2)) #checking the number of times 2 in the tuple


tuple1 = (3,2,34,49,30)
mylist = list(tuple1)
mylist.remove(34) #element to be removed by typecasting
tuple1 = tuple(mylist)
print(tuple1)