from pandas import *
from tkinter import *
from random import randint, choice

data_full = read_csv('./data/ukrainian_words.csv')

en_word = ''
try:
    data = read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data_full.to_csv('./data/words_to_learn.csv', index=False)
    data = read_csv('./data/words_to_learn.csv')

data_records = data_full.to_dict(orient='records')

def right_click():
    generate_card()


def wrong_click():
    generate_card()


# ---------------------------------- Flip Card --------------------------------------

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_text, text='English')
    global en_word
    canvas.itemconfig(word_text, text=en_word)


# ---------------------------------- Generate Card -----------------------------------

def generate_card():

    word = choice(data_records)
    ua_word = word['Ukrainian']
    global en_word, flip_timer
    window.after_cancel(flip_timer)
    flip_timer = window.after(3000, func=flip_card)
    en_word = word['English']
    canvas.itemconfig(language_text, text='Ukrainian')
    canvas.itemconfig(word_text, text=ua_word)
    canvas.itemconfig(canvas_image, image=card_front)




# ---------------------------- UI SETUP -----------------------------

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title('Flashy Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')

canvas_image = canvas.create_image(400, 260, image=card_front)

language_text = canvas.create_text(400, 100, text='Ukrainian', font=('Yrsa', 30, 'italic'))
word_text = canvas.create_text(400, 280, text='срака-мотика', font=('Yrsa', 100, 'bold'))
canvas.grid(column='0', row='0', columnspan='2')

image_right = PhotoImage(file='./images/right.png')
button_right = Button(image=image_right, command=right_click)
button_right.grid(column='1', row='1')

image_wrong = PhotoImage(file='./images/wrong.png')
button_wrong = Button(image=image_wrong, command=wrong_click)
button_wrong.grid(column='0', row='1')

generate_card()

window.mainloop()
