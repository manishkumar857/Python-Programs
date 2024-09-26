activity= []
def add_activity():
    ele = input("Enter your activity: ")
    activity.append(ele)
    print(f"{ele} is append in the list:")
def display():
     if(len(activity) == 0):
        print("list is empty!!")
        add_activity()
     else:
        print(activity)