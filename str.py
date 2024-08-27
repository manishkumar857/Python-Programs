import random
guess = random.randint(1,100)

i=0
while(True):
    
    x=int(input("guess the number between 1 to 100 enter number "))
    if(guess==x):
        print("you guessed it right number is ",guess)
        break
    elif(x>100 or x<1):
        print("number should be between 1 to 100")
    elif(x<guess):
        print(" your input is less than value ! Try again ")
    elif(x>guess):
        print("your input is greater than the value !Try again")
       
    i=i+1
    if(i==5 or i%5==0):
        y=int(input("do you want to play again 1 for yes and 0 for no "))
        if(y==0):
            break
        elif(y==1):
            continue
    
    
            
        
