# ---------------------------- LIBRARIES IMPORT ------------------------------- #
from tkinter import *
from tkinter import messagebox
import pandas
import random
from pandas.errors import EmptyDataError

BACKGROUND_COLOR = "#B1DDC6"
revamped_data = {}

# ---------------------------- FILE HANDLING ------------------------------- #
try:
    # Opening the words to learn csv file.
    words_to_learn_data = pandas.read_csv('data/words_to_learn.csv')
except EmptyDataError:
    # If the file doesn't exist or is empty, use the data in the original french csv file.
    original_data = pandas.read_csv('data/french_words.csv')
    revamped_data = original_data.to_dict(orient='records')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    revamped_data = original_data.to_dict(orient='records')
else:
    # If it does exist, convert it a list of dictionaries to be used in the code.
    revamped_data = words_to_learn_data.to_dict(orient='records')  # List of rows each in dictionary format.

global random_card


# ---------------------------- FLASHCARD CREATION & MOVEMENT ------------------------------- #


def next_flashcard():
    global random_card, flip_timer

    # Handling the case of if the buttons are pressed too quickly.
    window.after_cancel(flip_timer)  # Cancels the past card timer.

    try:
        # Displaying the next card operation.
        random_card = random.choice(revamped_data)
    except IndexError:
        # If revamped data list is empty, load the data from the original list and start all over.
        original = pandas.read_csv('data/french_words.csv')
        revamped_data.extend(original.to_dict(orient='records'))
        print(revamped_data)

    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(word, text=random_card['French'], fill='black')
    canvas.itemconfig(language, text='French', fill='black')

    # New timer initialized to flip current card.
    flip_timer = window.after(3000, switch_flashcard)  # Initializes a new timer.


def known_flashcard():
    revamped_data.remove(random_card)  # Removing the current card from the data if user has learnt it.
    # Convert the list of dictionaries to a dataframe and save it in the csv file for words to learn.
    words_to_learn = pandas.DataFrame(revamped_data)
    words_to_learn.to_csv('data/words_to_learn.csv', index=False)
    # Move on the next random flashcard generated.
    next_flashcard()


def switch_flashcard():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=random_card['English'], fill='white')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
# window.resizable(width=False, height=False)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=648, height=426, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(324, 213, image=card_front_img)

language = canvas.create_text(324, 100, text="", font=('Ariel', 40, "italic"))
word = canvas.create_text(324, 213, text="", font=('Ariel', 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_flashcard)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=known_flashcard)
right_button.grid(row=1, column=1)
messagebox.showinfo(message='Welcome to my Flashy Application!!!\nAfter 3 seconds, each flash card would flip to '
                            'show you the translation of the given word.\nIf you guessed right, click the right button,'
                            ' and if you did not, click the wrong button.\nGood luck :) ', title="Important Info")

flip_timer = window.after(3000, switch_flashcard)
next_flashcard()

window.mainloop()
