camarks = {10,20,30,25,19,29}
#print(camarks)
for i in camarks:
    print(i)
print(type(camarks))
#unodered , unchangeable and  not allow duplicates

Days=set(["a","b","c","d"])
print(Days)





camarks={'A','O','B','E'}
print(camarks)
print(type(camarks))

camarks1={'A',10,"B+",5.8,True}
print(camarks1)
#print(camarks1[0]) can't access sets like by index
print(type(camarks1))

# idx = int(input("enter the number "))
# camarks[0]=4 #they are unordered we can't change it 
# print(camarks) 

# camarks1.append(4)
# print(camarks1)

camarks1.add(7)
print(camarks1)
camarks1.pop()
print(camarks1)
camarks1.remove(7)
print(camarks1)
# camarks1.clear()
# print(camarks1)

ca = {1,1,1,1,2}
print(ca) #not allow duplicates

newset = camarks1.union(ca)
print(newset)