import random
import tkinter as tk
from tkinter import font


def roll_dice():
    number = random.randint(1, 6)

    if number == 6:
        number_label.config(text=f"{number}", fg="red")
    else:
        number_label.config(text=f"{number}", fg="black")


game_window = tk.Tk()
game_window.title("Dice Roller")
game_window.geometry("300x350")

title_font = font.Font(size=20)
number_font = font.Font(size=60)
btn_font = font.Font(size=12)

game_title = tk.Label(game_window, text="Roll the Dice!", font=title_font)
game_title.pack(pady=(20, 10))

number_label = tk.Label(
    game_window,
    text="0",
    font=number_font,
    fg="black",
)
number_label.pack(pady=30)

roll_btn = tk.Button(
    game_window,
    text="Roll Dice",
    width=15,
    bg="light blue",
    font=btn_font,
    command=roll_dice,
)
roll_btn.pack(pady=10)

game_window.mainloop()
