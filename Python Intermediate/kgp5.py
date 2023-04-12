e=open("even.txt","w")
o= open("odd.txt","w")
for i in range (1,101):
    if i%2 ==0:
        e.write(str(i))
        e.write("\n")
    else:
           print( o.write(str(i)))
        o.write("\n")
            e.close()
            o.close()
