roomtype={"super deluxe":10,"deluxe":25,"luxury":38,"standard":82}
print(roomtype)
checkindet = []

while True:
    x=int(input("select the options below : \n 1 for checkin\n 2 for check out \n 3 for list of guests"))
    if(x==1):
        print(roomtype)
        y=input("select your room type(in words)\n")
        name=input("enter your name ")
        # for a in roomtype:
        #     if(y==a):
        #         if(roomtype[a]>0):

        #             roomtype[a]=roomtype[a]-1
        #             print(a," room allocated")
        #             checkindet.append({"name":name,"room type":a})
        #         else:
        #            print("room doesnot exits")

        if y in roomtype:
            if(roomtype[y]>0):
                roomtype[y]=roomtype[y]-1
                print(y," room allocated")
                checkindet.append({"name":name,"room type":y})
            else:
                print("room doesnot exits")
        
    elif(x==2):
        print("check out menu ")
    elif(x==3):
        print(checkindet)


