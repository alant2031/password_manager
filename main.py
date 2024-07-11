# !/usr/bin/python3
# C:\Python312\python.exe

import tkinter as tk
from tkinter import messagebox
from pwd_module import generate
import pyperclip
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# ---------------------------- PASSWORD GENERATOR -------------------------- #


def generate_pwd():
    pwd = generate()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    pyperclip.copy(password)
    new_data = {website.lower(): {"login": login, "password": password}}

    if len(website) == 0 or len(password) == 0 or len(login) == 0:
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you have not left any fields empty.",
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \n\nLogin: {login}"
            + f"\nPassword: {password}\n\nIs it OK to save?",
        )

        if is_ok:
            try:
                with open(
                    os.path.join(BASE_DIR, "data.json"), "r"
                ) as data_file:
                    # Reading old data
                    data = json.load(data_file)

            except FileNotFoundError:
                with open(
                    os.path.join(BASE_DIR, "data.json"), "w"
                ) as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                # Check if website already exists and confirm
                if website.lower() in data:
                    msg = f"A website with name {website} already exists. "
                    confirm = messagebox.askyesno(
                        title=website,
                        message=msg + "Do you want to override it?",
                    )
                    if confirm:
                        # Updating old data with new data
                        data.update(new_data)
                        with open(
                            os.path.join(BASE_DIR, "data.json"), "w"
                        ) as data_file:
                            # Saving updated data
                            json.dump(data, data_file, indent=4)
                else:
                    data.update(new_data)
                    with open(
                        os.path.join(BASE_DIR, "data.json"), "w"
                    ) as data_file:
                        # Saving updated data
                        json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, tk.END)
                login_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)


# ---------------------------- FIND PASSWORD --------------------------- #
def find_pwd():
    website = website_entry.get()
    try:
        with open(os.path.join(BASE_DIR, "data.json")) as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")

    else:
        if website.lower() in data:
            appname = website.lower()
            login = data[appname]["login"]
            password = data[appname]["password"]

            pyperclip.copy(password)

            messagebox.showinfo(
                title=website,
                message=f"Login: {login}\nPassword copied to clipboard",
            )
        else:
            messagebox.showinfo(
                title="Not found", message=f"No details for {website} exists."
            )


# ---------------------------- LIST ACCOUNTS --------------------------- #
def show_values():
    try:
        with open(os.path.join(BASE_DIR, "data.json")) as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        return messagebox.showerror(
            title="Error", message="No Data File Found."
        )
    tx = ""
    for i, v in enumerate(data.keys()):
        tx += f"         {i+1}. {v}\n"

    formatted_text = f"-------------------------------\n\n{tx}\n-------------------------------"  # noqa
    messagebox.showinfo(title="Accounts", message=formatted_text)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.resizable(False, False)
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
tomato_img = tk.PhotoImage(file=os.path.join(BASE_DIR, "logo.png"))
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tk.Label(text="Website:", pady=8)
website_label.grid(column=0, row=1)
login_label = tk.Label(text="Login:")
login_label.grid(column=0, row=2)
password_label = tk.Label(text="Password:", pady=8)
password_label.grid(column=0, row=3)

# Entries
website_entry = tk.Entry()
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()
login_entry = tk.Entry()
login_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
login_entry.insert(0, "username/email")
password_entry = tk.Entry()
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
search_button = tk.Button(text="Search", width=9, command=find_pwd)
search_button.grid(row=1, column=2)

generate_button = tk.Button(text="Generate", command=generate_pwd)
generate_button.grid(column=2, row=3, sticky="EW")

list_button = tk.Button(text="List Accounts", command=show_values)
list_button.grid(column=0, row=4)

add_button = tk.Button(text="Save credentials", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

# https://riptutorial.com/tkinter/example/29713/grid--
