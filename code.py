import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")
    
    # Generate a random number between 1 and 50
    number_to_guess = random.randint(1, 50)
    attempts = 7 # Number of attempts the player has

    # Game loop
    for attempt in range(1, attempts + 1):
        print(f"\nAttempt {attempt} of {attempts}:")
        
        # Get user input
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # Check the guess
        if guess == number_to_guess:
            print("Congratulations! You guessed the correct number!")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print(f"\nSorry, you've used all your attempts. The correct number was {number_to_guess}.")

# Run the game
guess_the_number()