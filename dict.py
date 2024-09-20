dict1 = {
    "number" :1 ,
    "color" : "blue"
}
print(dict1)

print(dict1["color"])

dict1["color"]="Red"
print(dict1)

for key1 in dict1:
    #print(key1)
    print(key1,":",dict1[key1])

for values in dict1.values(): #accesing key values only with .values()
   print(values)

#square values from 0 to 10:
sq_value={}
for i in range(1,11):
    sq_value[i]=i**2
print(sq_value)

#check if key exist
n = int(input("enter the number for sq root : "))

for key1 in sq_value:
    #print(key1)
    if(n==key1):
        print("found");
        print(sq_value[key1])
        break
else:
    print("not found")
    
        
