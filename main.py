
from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP -----------------------------

window = Tk()
window.title('Flashy Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')

canvas.create_image(400, 260, image=card_front)
language_text = canvas.create_text(400, 150, text='Ukrainian', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='Срака-Мотика', font=('Arial', 40, 'italic'))
canvas.grid(column='0', row='0', columnspan='2')

image_right = PhotoImage(file='./images/right.png')
button_right = Button(image=image_right)
button_right.grid(column='1', row='1')

image_wrong = PhotoImage(file='./images/wrong.png')
button_wrong = Button(image=image_wrong, highlightthickness=0)
button_wrong.grid(column='0', row='1')

window.mainloop()

