# Hangman Game 🎮

A fun, interactive **Hangman Game** written in Python! Test your skills by guessing the country names before the hangman structure is fully drawn and your lives run out.

---

## How the Game Works
- You'll be provided with a word to guess, represented by underscores (`_`).
- Your task is to guess one letter at a time.
- **Correct guesses** reveal the positions of the guessed letter in the word.
- **Incorrect guesses** deduct one life, and the hangman structure progresses toward completion.
- You start with **7 lives**—use them wisely!

---

## Features
- **Random Country Selection**: A word is randomly chosen from the list of country names: `Canada`, `India`, `Italy`, `Australia`, `England`.
- **Interactive Gameplay**: Receive live feedback for each guess and see the current state of the hangman structure.
- **Hints**: The category is provided as a clue—guess the country name!
- **Win/Loss Conditions**: Guess the entire word to win, or lose if all lives are gone.

---

## Getting Started
### Prerequisites
- Python 3.x installed on your machine.
- Basic knowledge of running Python scripts.

### Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/rishavscripts/hangman-game.git
    ```
2. Navigate to the project directory:
    ```bash
    cd hangman-game
    ```

### Running the Game
1. Run the Python script:
    ```bash
    python hangman_game.py
    ```
2. Follow the instructions on the screen to play the game.

---

## Customization
- **Word List**: Add or modify words in the `words` list.
- **Lives**: Adjust the number of `lives` to increase or decrease game difficulty.

---

## File Structure
- `hangman_game.py`: Main game logic.
- `hangman_stages.py`: Contains visual representations of the hangman structure for each stage.

---

## Example Gameplay
```plaintext
Welcome to The Hangman Game.
Guess the word before the structure completes and lives are gone.
Hint: Country name.
['_', '_', '_', '_', '_', '_']
Enter your letter: a
Right guess. 7 lives remaining.
['_', 'a', '_', '_', 'a', '_']
...
You guessed it right. Game over. You win.
```

---

## Contribution
Feel free to fork this project, suggest enhancements, or report bugs via pull requests.

---


This README sets up your project clearly and professionally! Let me know if you'd like help customizing it further.
