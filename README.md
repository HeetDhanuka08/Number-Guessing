# Number Guessing Game

A simple Python console game where you try to guess a randomly selected number between 1 and 100. The game gives you hints after each guess, telling you if your guess is too high or too low, and how close you are!

## Features

- Input validation (handles invalid and out-of-range input)
- Guess counter (see how many tries you needed)
- Play again option
- Directional and distance-based hints (e.g., "Too high! You are very close!")

## How to Play

1. Run the script:
   ```bash
   python main.py
   ```
2. Enter your guess (a number between 1 and 100).
3. Follow the hints until you guess the correct number.
4. After winning, choose whether to play again.

## Requirements

- Python 3.x

## Example

```
I'm thinking of a number between 1 and 100.
Enter a number between 1 and 100: 50
Too low! You are very far!
Enter a number between 1 and 100: 75
Too high! You are close!
Enter a number between 1 and 100: 70
Too high! You are very close!
Enter a number between 1 and 100: 68
You guessed it Right! The number was 68.
It took you 4 guesses.
Do you want to play again? (y/n):