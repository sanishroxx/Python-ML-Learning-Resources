name=input("enter your name: ")
s=len(name)

temp=""
i=0
while i<s:
    if name[i] not in temp:
        temp=temp+name[i]
        print(f"{name[i]} : {name.count(name[i])}")
        i=i+1
    
    
