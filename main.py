import random

# Function to generate a random number between 1 and 100 
def getRandomNumber():
    return random.randrange(1, 100)

# Function to provide a specific hint based on the user's guess
def giveHint(number, guess):
    if guess == number:
        return "Correct!"
    direction = "Too low!" if guess < number else "Too high!"
    diff = abs(number - guess)
    if diff <= 2:
        proximity = "You are very close!"
    elif diff <= 5:
        proximity = "You are close!"
    elif diff <= 10:
        proximity = "You are a bit far!"
    elif diff <= 20:
        proximity = "You are far!"
    else:
        proximity = "You are very far!"
    return f"{direction} {proximity}"

# Main function to run the guessing game
# Handles input validation, guess counting, and replay option
def runGuess():
    while True:
        secretNumber = getRandomNumber()  # Generate a new secret number for each game
        guess_count = 0  # Initialize guess counter
        print("\nI'm thinking of a number between 1 and 100.")
        while True:
            try:
                user_input = int(input("Enter a number between 1 and 100: "))
                if not (1 <= user_input <= 100):  # Check if guess is within range
                    print("Please enter a number within the range 1 to 100.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue
            guess_count += 1  # Increment guess counter
            hint = giveHint(secretNumber, user_input)  # Get hint for the guess
            if hint == "Correct!":
                print(f"You guessed it Right! The number was {secretNumber}.")
                print(f"It took you {guess_count} guesses.")
                break  
            else:
                print(hint) 
                
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break  

# Entry point of the script
if __name__ == '__main__':
    runGuess()