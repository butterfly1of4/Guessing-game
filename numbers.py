import random

play = True
while play == True:
    guesses = []
    num = random.randint(0, 100)
    # print(num)
    print("It's time to guess the Number!\nPick a number between 1-100 to start. The computer will give you clues to how close you are to guessing correctly.")
    for i in range(0, 100):
        guess = input("\nGuess a number: ")
        # print(guess)
        guess = int(guess)
        if guess == num:
            guess == num
            # print(num, guess)
            print("You guessed it!")
    # print(guesses)
            break
        elif guess != num:
            # print(num, guess)
            print("Guess again,")
            if abs(num-guess) >= 50:
                guesses.append(guess)
                print("You are more than 50 away \n")
            elif abs(num-guess) < 50 and abs(num-guess) > 25:
                guesses.append(guess)
                print("Your guess was between 50 and 25 away \n")
            elif abs(num-guess) < 25 and abs(num-guess) > 10:
                guesses.append(guess)
                print("You are 10-25 away \n")
            elif abs(num-guess) < 10:
                guesses.append(guess)
                print("Within 10 \n")
            elif abs(num-guess) < 5:
                guesses.append(guess)
                print("Within 5")
            else:
                guesses.append(guess)
        print("Your guesses: ",guesses)
    print(
        "The random number was", num,". You guessed the number in " f'{len(guesses)}' " tries. Would you like to play again?")
    play_again = input("Yes or No: ")
    if play_again == "yes":
        play == True
        continue
    else:
        play == False
        print("Goodbye")
        break
else:
    play == False
