# camarks = {10,20,30,25,19,206,29}
# #print(camarks)
# for i in camarks:
#     print(i)
# print(type(camarks))
# #unodered , unchangeable and  not allow duplicates

# camarks1={'A',10,"B+",5.8,True}
# print(camarks1)
# #print(camarks1[0]) can't access sets like by index
# print(type(camarks1))


# # idx = int(input("enter the number "))
# # camarks[0]=4 #they are unordered we can't change it 
# # print(camarks) 

# # camarks1.append(4)
# # print(camarks1)

# Days=set(["a","b","c","d"])
# print(Days)


# #set which have immutable elements
# set1={1,2,3,"hello,20.5"}
# print(set1)

#mutable elements like list are not allowed inside sets

#add() add only single item and with update() mutiple elemnts

# camarks={'A','O','B','E'}
# print(camarks)

# camarks.add("new")
# print(camarks)
# camarks.update(["new1","new2"])
# print(camarks)


# camarks.discard("new")
# camarks.remove("new1")
# print(camarks)
# camarks.discard("new")
# #camarks.remove("new1") #it will show error if element not present (not in case of discard this happens)
# #camarks(print)



# camarks1={'A',10,"B+",5.8,True}
# camarks1.add(7)
# print(camarks1)
# camarks1.pop()
# print(camarks1)
# camarks1.remove(7)
# print(camarks1)
# camarks1.clear()
# print(camarks1)

# ca = {1,1,1,1,2}
# print(ca) #not allow duplicates

# newset = camarks1.union(ca)
# print(newset)

# Days1={"mon","tues","wed","thur","sun"}
# Days2={"fri","sat","sun"}
# print(Days1|Days2)

# Days1={"mon","tues","wed","thur","sun"}
# Days2={"fri","sat","sun"}
# print(Days1&Days2)

# Days1.intersection_update(Days2)
# print(Days1)

# Days1={"mon","tues","wed","thur","sun"}
# Days2={"fri","sat","sun"}
# print(Days1-Days2)


Days1={"mon","tues","wed","thur","sun"}
Days2={"fri","sat","sun"}
print(Days1.difference(Days2))

a={1,2,3,4,5,6}
b={1,2,9,8,10}
c=a^b
print(c) #symmetric difference