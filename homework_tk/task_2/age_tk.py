import tkinter as tk
from tkinter import messagebox, END, Tk, Label, Entry, Button, Radiobutton, StringVar
from datetime import datetime
from tkcalendar import DateEntry

wn = tk.Tk()
wn.geometry("300x200")
wn.configure(background='cyan')
wn.title("age calculator")


def get_age(age):
    print(age)
    label3 = Label(wn, text=f'Your age {23 - age}', background='cyan')
    label3.grid()
    return age


# text
label = Label(wn, text='Age calculator', background="cyan", fg='blue')
label.grid(pady=20, column=4, row=2)

# date brith
label1 = Label(wn, text='Your brith day', background="green", fg='cyan')
label1.grid(padx=16, column=2, row=3)
date_brith = DateEntry(wn)
date_brith.grid(row=3, column=4)


def get_a():
    get_age(int(date_brith.get()[-2:]))


# button

button = Button(wn, text='Next->', background='yellow', borderwidth=1, command=get_a)
button.grid(padx=10, column=4, pady=30)

if __name__ == '__main__':
    wn.mainloop()
