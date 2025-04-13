import random

def guess_the_number():

    number_to_guess = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")
    
    
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts!")
            break

guess_the_number()
