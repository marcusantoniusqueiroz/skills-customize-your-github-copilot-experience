# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game using Python, practicing string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Implement the Hangman Game

#### Description
Create a fully playable Hangman game where the player guesses letters one at a time to reveal a hidden word before running out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list using the `random` module.
- Display the current guessed state of the word using underscores (e.g., `_ _ _ _ _`).
- Accept a single letter as input from the player each turn.
- Reveal correctly guessed letters in their proper positions.
- Track and display the number of incorrect guesses remaining.
- End the game when the word is fully guessed (win) or attempts are exhausted (lose).
- Display an appropriate win or lose message at the end. Example:
  ```
  Word: _ _ _ _ _
  Guess a letter: a
  Word: _ a _ _ _
  Incorrect guesses remaining: 5
  ...
  You win! The word was: magic
  ```
