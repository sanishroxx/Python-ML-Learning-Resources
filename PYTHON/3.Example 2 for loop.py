#practice for loop
#ask user a number
#calculate sum of digits

total=0
n=input("enter a number")
for i in range(0,len(n)):
    total=total+int(n[i])
print(total)
