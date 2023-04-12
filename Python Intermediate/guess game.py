import random
guessesTaken=0
print("hello! what is your name?")
myName=input()
number=random.randint(1, 20)
print("i am sam thinking no between 1 to 20")
for guessesTaken in range(15):
    print("take a guess")
    guess=input()
    guess=int(guess)
    if guess < number:
        print("your guess is  too low")
        if guess > number:
            print("your guess is too high")
