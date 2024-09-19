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

for values in dict1.values():
   print(values)