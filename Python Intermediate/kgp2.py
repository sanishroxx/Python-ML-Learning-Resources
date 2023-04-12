hello = [1,2,3,4,5,6,"kgp",9.0]
print(hello[::2])


name="namsate duniya "
clist = name.split(" ")
print(clist)

count = 0
for item in clist:
    if item==item[::-1]:
        count=count+1
        print("palindrom count is " , count)
num=12
check=int(str(int(math.sqrt(int((str(num**num)[::-1])))))[::-1])
if num==check:
    print("Adome")
else:
        print("Not Adome")



        
    
