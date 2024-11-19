account={
    "name":"Manish",
    "balance":100
}

account2={
     "name":"Akash",
     "balance":30
}

print(account)

class Error(Exception):
    pass
class NegativeNumber(Error):
    pass



y=int(input("enter 1 to depoist money \n enter 2 to withdraw money"))
if(y==1):
     
    while True:
            
            try:
                number=int(input("enter the number"))
                
                if number<0:
                    raise NegativeNumber
            
                    break
                elif number>0:
                    print(account)
                    account["balance"]=account["balance"]+number
                    print(account)
                    break
            except NegativeNumber:
                print("value is negative")

elif(y==2):
     while True:
            
            try:
                number=int(input("enter the number"))
                
                if number<0:
                    raise NegativeNumber
                    
                    break
                elif number>0:
                    print(account)
                    account["balance"]=account["balance"]-number
                    print(account)
                    break
            except NegativeNumber:
                print("withdrawn account is negative")


          


            

     




        



           

    
    
            





