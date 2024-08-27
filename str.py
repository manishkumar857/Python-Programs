import random
guess = random.randint(1,100)
print("guess the number between 1 to 100")
x=int(input("enter number "))
if(guess==x):
    print("you guessed it right number is ",guess)
elif(x>100 or x<1):
    print("number should be between 1 to 100")
else:
    print("try again")
    print("number is ",guess)
