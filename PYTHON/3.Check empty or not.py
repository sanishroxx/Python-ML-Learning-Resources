#check empty or not

name="prince"
if name:  #true if string is not empty
    print("string is not empty")
else:
    print("string is empty")


name=""
if name:  
    print("string is not empty")
else:
    print("string is empty")



name=input("enter your name: ")
if name:
    print(f"your name is {name}")
else:
    print("you didn\'t type anything")
