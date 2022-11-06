from tkinter import Button, Label, Tk
from tkinter.ttk import Entry


def change_label():
    name = entry.get()
    label.config(text=f"Привет, {name}!")


win = Tk()
win.title("Учебный пример")
win.geometry("400x300")

text = "Привет, всем!"
font = ('Arial', 30)
label = Label(win, text=text, font=font)
label.pack(pady=10)

font = ('Arial', 14)
entry = Entry(win, font=font)
entry.pack(pady=10)

text = "Нажми меня"
font = ('Arial', 14)
button = Button(win, text=text, font=font, command=change_label)
button.pack(pady=10)

if __name__ == '__main__':
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    finally:
        win.mainloop()
