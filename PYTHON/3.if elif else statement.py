#if elif else statement
#show ticket price
#0 to 3 (free)
#4 to 10 (150)
#11 to 60 (250)
#above 60 (200)

age=input("please input your age: ")
age=int(age)

if 0<age<=3:
    print("Ticket Price: Free")
elif 3<age<=10:
    print("Ticket Price: 150")
elif 10<age<=60:
    print("Ticket Price: 250")
else:
    print("Ticket Price: 200")
