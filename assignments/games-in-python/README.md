# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game in Python to practice strings, loops, conditionals, and user input. The game should let a player guess a randomly selected word before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the word list and game state, then show the player the hidden word as underscores.

#### Requirements
Completed program should:

- Select a word at random from a predefined list.
- Display one underscore for each letter in the selected word, separated by spaces (for example, `_ _ _ _`).
- Track the letters the player has guessed and the number of incorrect guesses remaining.

### 🛠️ Play a Round of Hangman

#### Description
Prompt the player to guess letters and update the game until the word is guessed or no attempts remain.

#### Requirements
Completed program should:

- Accept a letter guess from the player on each turn.
- Reveal each matching letter in its correct position in the displayed word.
- Reduce the remaining attempts for each incorrect guess and display the updated word progress and attempts.
- End when the player guesses the word or runs out of attempts.
- Display a win message when the word is guessed and a lose message when attempts are exhausted.
