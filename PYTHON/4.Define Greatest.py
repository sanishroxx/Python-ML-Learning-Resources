def greatest(a,b,c):
    if a>b and a>c:
        print(f"{a} is greatest number")
        return a
    elif b>a and b>c:
        print(f"{b} is greatest number")
        return b
    else:
        print(f"{c} is greatest number")
        return c
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
greatest(a,b,c)
