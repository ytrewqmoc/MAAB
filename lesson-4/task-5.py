import random

def play_game():
    number = random.randint(1, 100)
    attempts = 10

    while attempts > 0:
        try:
            guess = int(input(f"You have {attempts} attempts left. Enter your guess (1-100): "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
            else:
                print("You guessed it right!")
                return

            attempts -= 1

        except ValueError:
            print("Invalid input! Please enter a number.")

    print("You lost. Want to play again?")
    retry = input("Type 'Yes' to play again: ")
    
    if retry in ['Y']:
        play_game()

play_game()
