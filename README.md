# Flashy - Flashcard Learning Application

## Project Overview

Flashy is a Python-based flashcard application designed to help users learn French vocabulary. The application uses Tkinter for the graphical user interface (GUI) and Pandas for data handling. Flashy displays French words on flashcards and, after a short delay, flips the card to show the English translation. Users can mark words as known or unknown, and their progress is saved automatically.

## Features

1. **Flashcard Display**: Show flashcards with French words, flipping to the English translation after a delay.
2. **Progress Tracking**: Track known and unknown words, saving progress in a CSV file.
3. **Data Handling**: Load vocabulary from a CSV file and update it dynamically based on user interactions.
4. **User Interaction**: Buttons to indicate whether a word is known or unknown, influencing the next flashcard displayed.

## Dependencies

- Python 3.x
- Tkinter (comes pre-installed with Python)
- Pandas (for data handling)

## File Descriptions

### `main.py`

This file contains the main logic and GUI setup for the flashcard application. It includes functions for handling flashcard display, flipping cards, and tracking known words.

### `data/french_words.csv`

The initial dataset containing French words and their English translations.

### `data/words_to_learn.csv`

A dynamically updated file that tracks the words the user has not yet learned.

### `images/card_front.png` and `images/card_back.png`

Images used for the front and back of the flashcards.

### `images/right.png` and `images/wrong.png`

Images used for the buttons to mark words as known or unknown.

## Getting Started

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Install Dependencies**: Ensure all dependencies are installed. You can install Pandas using pip:
   ```bash
   pip install pandas
   ```

3. **Run the Project**: Execute the `main.py` file to start the application.
   ```bash
   python main.py
   ```

## Usage

1. **Start the Application**: When you run the application, a flashcard will be displayed with a French word.
2. **Flip the Card**: After 3 seconds, the card will flip to show the English translation.
3. **Mark as Known/Unknown**: Use the right button (known) or wrong button (unknown) to indicate whether you knew the word.
4. **Progress Saving**: Your progress is saved automatically in the `data/words_to_learn.csv` file.

## Code Explanation

### File Handling

The application attempts to load the `words_to_learn.csv` file. If the file is empty or does not exist, it falls back to the initial dataset from `french_words.csv`.

### Flashcard Creation and Movement

The `next_flashcard` function handles displaying the next flashcard. It cancels the previous timer and sets a new one to flip the card.



### Known Flashcard

The `known_flashcard` function removes the current card from the list of words to learn and updates the CSV file.


### UI Setup

The UI setup uses Tkinter to create the main window, canvas, labels, and buttons.


## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure your code follows the project’s coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

This comprehensive readme should help you understand the structure and functionality of my Flashy application. If you have any questions or need further assistance, please feel free to ask :)
