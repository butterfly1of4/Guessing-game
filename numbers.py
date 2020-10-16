import random

play = True
while play == True:
    guesses = []
    num = random.randint(0, 100)
    print(num)

    for i in range(0, 100):
        guess = input("Guess a number: ")
        print(guess)
        guess = int(guess)
        if guess == num:
            guess == num
            print(num, guess)
            print("You guessed it!")
    # print(guesses)
            break
        elif guess != num:
            print(num, guess)
    # print(guesses)
            print("Guess again")
        guesses.append(guess)

    print(guesses, len(guesses))
    print(
    "You guessed the number in " f'{len(guesses)}' " tries. Would you like to play again?")
    play_again = input("Yes or No: ")
    if play_again == "yes":
        play==True
        continue
    else: 
        play == False
        print("Goodbye")
        break
else: 
    play == False