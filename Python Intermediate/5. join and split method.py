#split method
#convert string to list
user_info='Prince 18'.split()
print(user_info)

user_info='Prince,18'.split(',')
print(user_info)

name,age='Prince,18'.split(',')
print(name)
print(age)

name,age=input("enter your name and age").split(',')
print(name)
print(age)

#join method
#convert list into string
user_info=['Prince','18']
print(','.join(user_info))


