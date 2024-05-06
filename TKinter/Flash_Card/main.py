from tkinter import *
import pandas
import random

BACKGROUND = '#b1ddc6'
current_card = {}
learn = {}

# ------------------------------ LEARN LIST ------------------------------- #

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    og_data = pandas.read_csv('data/words.csv')
    print(og_data)
    learn = og_data.to_dict(orient='records')
else:
    learn = data.to_dict(orient='records')


def is_known():
    learn.remove(current_card)
    print(len(learn))
    Data = pandas.DataFrame(learn)
    Data.to_csv('data/words_to_learn.csv', index=False)

    next_card()


# ------------------------------ FLIP CARD -------------------------------- #

def flip():
    canvas.itemconfig(card_title, text='המשמעות', fill='white')
    canvas.itemconfig(card_word, text=find_break(current_card['Explanation']), fill='white')
    canvas.itemconfig(card_background, image=back)


# ---------------------------- CREATE WORDS ------------------------------- #
# data = pandas.read_csv('data/words_to_learn.csv')
# learn = data.to_dict(orient='records')
#


def next_card():
    global current_card, timer
    win.after_cancel(timer)
    current_card = random.choice(learn)
    canvas.itemconfig(card_title, text='המילה', fill='black')
    canvas.itemconfig(card_word, text=current_card['Word'], fill='black')
    canvas.itemconfig(card_background, image=front)
    timer = win.after(5000, flip)


# ---------------------------------- UI ----------------------------------- #

def find_break(word):
    new_word = ''
    for i in range((len(word) // 15) + 1):
        new_word += word[word.find(' ', 15 * i): word.find(' ', 15 * (i + 1))] + '\n'

    return new_word.rstrip() + word[-1]


win = Tk()
win.title('עברית פסיכומטרי')
win.config(padx=50, pady=50, bg=BACKGROUND)

timer = win.after(5000, flip)

canvas = Canvas(width=800, height=526)
front = PhotoImage(file='img/card_front.png')
back = PhotoImage(file='img/card_back.png')
card_background = canvas.create_image(400, 263, image=front)

card_title = canvas.create_text(400, 130, text='', font=('Arial', 50, 'bold'))
card_word = canvas.create_text(400, 303, text='', justify="center", font=('Arial', 40, 'italic'))
canvas.config(bg=BACKGROUND, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file='img/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file='img/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

win.mainloop()
