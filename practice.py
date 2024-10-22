food = {
    "butter" : 120,
    "sandwich":340,
    "milk":250
}

while True:
    
    def add():
        x=input("enter the food type ")                                         
        if x not in food:
            y=int(input("enter the food price "))
            food[x]=y
            print(food)

    def update():
        x=input("enter food type which you want to update ")
        if x in food:
            p=int(input("enter the updated price "))
            food[x] = p
        else:
            print("food item doesnot exits")

    def display():
        for key,val in food.items():
            print("item:",key," ","price:",val)

    def thres():
        t=int(input("enter the threshold price:"))
        for x in food:
            if(food[x]>t):
                print(x ," ",food[x])


    x=int(input("select 1 to add\n select 2 to update price\nselect 3 to display\n 4 for threshold price"))
    if(x==1):
        add()
    elif(x==2):
        update()
    elif(x==3):
        display()
    elif(x==4):
        thres()