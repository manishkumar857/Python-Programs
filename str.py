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

str ="welcome to the world of programming "
a = str[3:7]
print(a)

randomstr ="this is python class"
print(type(randomstr))

print(randomstr[0])
print(randomstr[-1])

