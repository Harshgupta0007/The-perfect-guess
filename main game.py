# THE PERFECT GUESS GAME BY HARSH GUPTA
def perfect_guess():
    import random
    rand = random.randint(1, 100)
    count = 0
    total_guess = 10
    print("WELCOME TO THE PERFECT GUESS GAME BY HARSH GUPTA")
    print("ENTER YOUR GUESS AND LET'S SEE IF YOU HAVE A PERFECT GUESS!!")
    print("Guess a number between 1 to 100")
    print("You have 10 number of guesses")
    while 1:
        guess = int(input("Enter your guess::"))
        count += 1
        total_guess -= 1
        if total_guess == 0:
            print("You lost the game. Try again!!")
            print("Do you want to play again?\nPress Y to play again.\nPress N to exit")
            choice = input()
            if choice == 'Y' or choice == 'y':
                perfect_guess()
            elif choice == 'N' or choice == 'n':
                break
            else:
                print("Please enter valid input")
                break
        elif guess > rand:
            print("Enter small number. Your guessed number is high.")
            print(total_guess, "chances left")
        elif guess < rand:
            print("Enter big number. Your guessed number is low.")
            print(total_guess, "chances left")
        else:
            print(f"You guessed it right in {count} times")
            print("Do you want to play again?\nPress Y to play again.\nPress N to exit")
            choice = input()
            if choice == 'Y' or choice == 'y':
                perfect_guess()
            elif choice == 'N' or choice == 'n':
                break
                exit()
            else:
                print("Please enter valid input")
                break
                exit()


perfect_guess()
