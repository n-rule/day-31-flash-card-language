from pandas import *
from tkinter import *

data = read_csv('ukrainian_words.csv')
# data = DataFrame.to_dict(orient='records')

def right_click():
    pass


def wrong_click():
    pass



# ---------------------------------- Generate Card -----------------------------------


def generate_card():
    pass


# ---------------------------- UI SETUP -----------------------------

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title('Flashy Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')

canvas.create_image(400, 260, image=card_front)
language_text = canvas.create_text(400, 150, text='Ukrainian', font=('Yrsa', 40, 'italic'))
word_text = canvas.create_text(400, 300, text='Срака-Мотика', font=('Yrsa', 60, 'bold'))
canvas.grid(column='0', row='0', columnspan='2')

image_right = PhotoImage(file='./images/right.png')
button_right = Button(image=image_right, command=right_click)
button_right.grid(column='1', row='1')

image_wrong = PhotoImage(file='./images/wrong.png')
button_wrong = Button(image=image_wrong, command=wrong_click)
button_wrong.grid(column='0', row='1')

window.mainloop()


