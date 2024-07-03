import random
def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    # Initialize number of guesses and previous guess
    num_guesses = 0
    previous_guess = None
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if guess < 1 or guess > 100:
                print("Please enter a number within the valid range (1-100).")
                continue
            num_guesses += 1
            # Provide hints to the player
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {num_guesses} guesses.")
                break
            # Check if the player is getting closer or farther from the number
            if previous_guess is not None:
                distance_current = abs(secret_number - guess)
                distance_previous = abs(secret_number - previous_guess)
                if distance_current < distance_previous:
                    print("You are getting closer to the number!")
                elif distance_current > distance_previous:
                    print("You are getting farther from the number.")

            previous_guess = guess
        except ValueError:
            print("Invalid input! Please enter a valid number.")
if __name__ == "__main__":
    guess_number()
