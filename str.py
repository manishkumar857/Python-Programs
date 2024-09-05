'''str = "welcome to python "
    for i in str:
    print(i,end="")


print(end="\n")
i=0
while(i<len(str)):
    print(str[i],end="")
    i=i+1


#reversing a string
i=len(str)-1
while(i>=0):
    print(str[i],end="")
    i=i-1'''

#strings are immuatble ie cannot be changed
#from reverse inex starts from -1 ,-2......

'''x = int(input("Enter the last number: "))
ch = ord('A')  

for i in range(x):
    for j in range(i + 1):
        current_ascii = ch + j  
        print(chr(current_ascii), end=" ")  
    print() '''

#slicing 

'''str ="welcome to the world of programming "
a = str[3:7]
print(a)

randomstr ="this is python class"
print(type(randomstr))

print(randomstr[0])
print(randomstr[-1])
#reverse
print(randomstr[::-1])'''

#random = 'this is python "3.0" '
'''random = " tHIS this is python \"3.0\""
print(random)

print(random.upper()) #uppercase string
print(random.lower()) #lowercase string

randoms = " THIS this is python \"3.0\""
print(randoms.capitalize())
print(randoms.title())
property(randoms.strip()) #to remove the space from leading and trailing parts'''

#find any words in any string
randomstr = "this is python"
findword = input("enter the word you want to find in string")
resp = randomstr.find(findword)
print(resp)

if(resp==1):
    print("word found")
else:
    print("not found")

valwords  = input("enter your phone number")
if(valwords.isdigit()): #check if inputs is of digit only
    print("valid input")
else:
    print("invalid input")

valword  = input("enter your phone number")
if(valword.isalnum()): #check if inputs is of digit and alpha
    print("valid input")
else:
    print("invalid input")

