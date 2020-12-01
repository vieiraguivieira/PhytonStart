answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input()) #usei int para converter o string

if guess < answer:
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("You guessed it")
    else:
        print("Sorry, you have not guessed correctly")
elif guess > answer:
    print("Please guess lower")
    if guess == answer:
        print("You guessed it")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it first time")
