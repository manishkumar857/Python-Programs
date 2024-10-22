import datetime

details= {
    'Antriksh':24,
    'Manish':5,
    'Harsh':100
}
from datetime import date

today = date.today()
print("Current Date:", today)

withdrawaldetails = []
depdetails=[]

while True:
    

    def withdraw(y,amount):
        for key1 in details:
            if(key1==y):
                if(amount>details[key1]):
                    print("insufficent balance ")
                    break
                details[key1]=details[key1]-amount
                print("new balance is ",details[key1])
                withdrawaldetails.append({"name": key1,"amount withdrawn":amount})
                print(withdrawaldetails)

    def depoist(y,amount):
        for key1 in details:
            if(key1==y):
                
                details[key1]=details[key1]+amount
                print("new balance is ",details[key1])
                newdate = f"{today.year}-{today.month}-{today.day}"
                depdetails.append({"name": key1,"amount deposited":amount,"date":newdate})
                print(depdetails)



    x=int(input("enter 1 to withdraw \nenter 2 to depost\nenter 3 to display\nenter 4 to exit"))
    if(x==1):
        y=input("enter the name of user ")
        amount=int(input("enter the amount you want to withdraw "))
        withdraw(y,amount)
    elif(x==2):
        y=input("enter the name of user ")
        amount=int(input("enter the amount you want to depoist "))
        depoist(y,amount)
    elif(x==3):
        for key,val in details.items():
            print("name",key,"value",val)
    elif(x==4):
        break
    else:
        print("wrong input")
        continue



