import csv
import os
from datetime import datetime
from tkinter import messagebox, END, Tk, Label, Entry, Button, Radiobutton, StringVar
from tkcalendar import DateEntry

from hotelr import Hotel

window = Tk()
window.title("Student Registration")
window.geometry("500x400")
window.configure(bg='pink')
hotel_p = []


def add(c=True):
    hotels = Hotel(
        fullname_entry.get(),
        money_entry.get(),
        age_entry.get(),
        phone_entry.get(),
        day_h_entry.get(),
        country_entry.get()

    )
    for i in hotels.get_hotel(as_dict=True).values():
        if i == '':
            c = False
    if c:
        hotel_p.append(hotels.get_hotel(as_dict=True))
        messagebox.showinfo("Information", "The data has been added successfully")
        clear()
    else:
        messagebox.showerror("no argument", "no argument")


def save():
    with open('hotelp.cvs', "a", newline="\n") as file:
        header = ["Fullname", "money", "age", "phone", "day_h", "country"]
        csv_writer = csv.DictWriter(file, header)
        if os.path.getsize('hotelp.cvs') == 0:
            csv_writer.writeheader()
            if len(hotel_p) == 0:
                messagebox.showerror("first add", "you must to first add do not SAVE ")
            else:
                csv_writer.writerows(hotel_p)
                messagebox.showinfo("Information", "Saved successfully")
        else:
            if len(hotel_p) == 0:
                messagebox.showerror("first add", "you must to first add do not SAVE ")
            else:
                csv_writer.writerows(hotel_p)
                messagebox.showinfo("Information", "Saved successfully")


def clear():
    fullname_entry.delete(0, END)
    money_entry.delete(0, END)
    age_entry.delete(0, END)
    phone_entry.delete(0, END)
    day_h_entry.delete(0, END)
    phone_entry.delete(0, END)
    country_entry.delete(0, END)


# Fullname
fullname_label = Label(window, text="Fullname: ", padx=20, pady=10, fg='orchid', bg='pink')
fullname_label.grid(row=0, column=0)
fullname_entry = Entry(window, width=30, borderwidth=2, bg='white')
fullname_entry.grid(row=0, column=1)

# money
money_label = Label(window, text="Money: ", padx=20, pady=10, fg='orchid', bg='pink')
money_label.grid(row=1, column=0)
money_entry = Entry(window, width=30, borderwidth=3)
money_entry.grid(row=1, column=1)

# age
age_label = Label(window, text="Age: ", padx=20, pady=10, fg='orchid', bg='pink')
age_label.grid(row=2, column=0)
age_entry = DateEntry(window)
age_entry.grid(row=2, column=1)

# Phone
phone_label = Label(window, text="Phone: ", padx=20, pady=10, fg='orchid', bg='pink')
phone_label.grid(row=4, column=0)
phone_entry = Entry(window, width=30, borderwidth=3)
phone_entry.grid(row=4, column=1)

# day_h
day_h_label = Label(window, text="day hotel: ", padx=20, pady=10, fg='orchid', bg='pink')
day_h_label.grid(row=5, column=0)
day_h_entry = Entry(window, width=30, borderwidth=3)
day_h_entry.grid(row=5, column=1)

# country
country_label = Label(window, text="country: ", padx=20, pady=10, fg='orchid', bg='pink')
country_label.grid(row=6, column=0)
country_entry = Entry(window, width=30, borderwidth=3)
country_entry.grid(row=6, column=1)

# Save button
save_btn = Button(window, text="Save", padx=20, pady=10, command=save, bg='green')
save_btn.place(x=60, y=250)

# Add button
add_btn = Button(window, text="Add", padx=20, pady=10, command=add, bg='yellow')
add_btn.place(x=140, y=250)

# Clear button
clear_btn = Button(window, text="Clear", padx=18, pady=10, command=clear, bg='cyan')
clear_btn.place(x=215, y=250)

# Exit button
exit_btn = Button(window, text="Exit", padx=20, pady=10, command=window.quit, bg='red')
exit_btn.place(x=295, y=250)

if __name__ == "__main__":
    window.mainloop()
