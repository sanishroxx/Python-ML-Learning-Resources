#practice for loop
#ask user name and count each character
#"prince kumar"

name=input("enter your name: ")
temp=""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp=temp+name[i]
        
    
