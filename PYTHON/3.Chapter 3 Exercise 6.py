winning_number=62
guess = 1
number = int(input("guess a number between 1 and 100: "))
game_over = False

while not game_over:
    if number == winning_number:
        print(f"you win, and you guessed this number in {guess} times")
        game_over = True
    else:
        if number<winning_number:
            print("Too Low")
            guess=guess+1
            number=int(input("Guess Again: "))
        else:
            print("Too High")
            guess=guess+1
            number=int(input("Guess Again: "))
