#scope
x=5
def func():
    global x
    x=7 #local variables
    return x
print(x)
print(func())
print(x)
