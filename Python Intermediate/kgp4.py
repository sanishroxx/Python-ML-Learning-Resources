import time
f1=open("demo.txt","w")
print(f1.write("this is my first sample part"))
time.sleep(5)
print(f1.close())
time.sleep(5)
f2=open("demo.txt","r")
print(f2.read())
f2.close()
