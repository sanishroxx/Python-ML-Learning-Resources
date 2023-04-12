#1.replace method
string="she is beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was"))
print(string.replace("is","was",1))  #replace only 1 is
print(string.replace("is","was",2))  #replace Both 2 is

#2.find() method

print(string.find("is"))
print(string.find("is",0))
print(string.find("is",5))

is_pos1=string.find("is") #is_pos1----->number
is_pos2=string.find("is",is_pos1 + 1)
print(is_pos2)
