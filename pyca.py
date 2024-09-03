print("items available for purchase : ")
print("Soap item id =1 Price =100\nBook Item id =2 Price = 6000\nMobile Item id =3 Price = 60000")

print("\n")
items=int(input("enter the number of items you purchased out of 3 : "))

i=0
cost=0
while(True):
    var1 =int(input("enter the item id "))
    var2=int(input("enter the Quantity "))


    if(var1==1):

        cost = cost +100 
        cost = cost * var2
        
    if(var1==2):
        cost=cost+6000
        cost = cost * var2
        

    if(var1==3):
        cost=cost+60000
        cost = cost * var2
         
    i=i+1
    if(i==items):
        break
print("Total cost is : ",cost,"\n total items purchased is ",items)


if(cost <= 5000):
    print("Sorry No Discount ! Available")
elif(cost>5000 and cost<10000):  
    print(" 10 % discount available ")
    discount10 = cost/10
    print("discount given ",discount10)
    cost = cost -discount10
    print("final price is " , cost)
elif(cost>10000):
    print("15 % discount available ")
    discount10 = cost/10
    discount5 =discount10/5
    discount15 = discount10+discount5
    print("discount given ",discount15)
    cost = cost - discount5
    print("final price to be paid : ",cost)

#other question

    
'''salamount = int(input("enter the sales amount : "))
commission=0
if(salamount>1000):
    commission=salamount/10
    print(commission)
elif(salamount<=1000 and salamount>500):
    commission=salamount/5
    print(commission)
elif(salamount>=500):
    print("no commission")'''