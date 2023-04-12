def greatest(a,b):
    if a>b:
        print(f"{a} is greatest number")
        return a
    else:
        print(f"{b} is greatest number")
        return b
a=int(input("enter first number"))
b=int(input("enter second number"))

greatest(a,b)


#=========OR==========

def greater(a,b):
    if a>b:
        return a
    else:
        return b
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))

bigger=greater(num1,num2)
print(f"{bigger} is greater")
