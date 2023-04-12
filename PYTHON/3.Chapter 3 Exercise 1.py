winning_number=12
guess_number=int(input("please guess a number: "))
if guess_number == winning_number:
    print("YOU WIN!!!!")
else:
    if guess_number > winning_number:
        print("too high")
        
    else:
         print("too low")
    

