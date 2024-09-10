ls = [2,2,4,5,5,6] # list are mutable , it allows duplicates values
print(ls)

ls.append(2) #can add only one argument
print(ls)
ls.append(2)

ls2=[3,3,3,3,3,3]
ls.extend(ls2)
print(ls)

ls.insert(0,76) #index,value
print(ls)

