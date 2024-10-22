details= {
    'Antriksh':24,
    'Manish':5,
    'Harsh':100
}




while True:
    

    def withdraw(y,amount):
        for key1 in details:
            if(key1==y):
                if(amount>details[key1]):
                    print("insufficent balance ")
                    break
                details[key1]=details[key1]-amount
                print("new balance is ",details[key1])

    x=int(input("enter 1 to withdraw \nenter 2 to depost\nenter 3 to displaay\nenter 4 to exit"))
    if(x==1):
        y=input("enter the name of user ")
        amount=int(input("enter the amount you want to withdraw "))
        withdraw(y,amount)

    if(x==4):
        break



