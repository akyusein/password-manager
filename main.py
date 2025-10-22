from tkinter import *
from tkinter import messagebox
import pyperclip
import json
from utils import *
# ---------------------------- SEARCH CREDENTIALS ------------------------------- #
def search_credentials():
    website = website_text.get()
    try:
        with open("entries.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Error", message="The Database Doesn't Exist!")
    except KeyError:
        messagebox.showinfo(title=f"Error", message="Credentials Don't Exist For This Website!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\n Password: {password}")
        elif website == '':
            messagebox.showinfo(title=f"Error", message="The Website Field is Empty!")
        else:
            messagebox.showinfo(title=f"Error", message="Credentials Don't Exist For This Website!")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    new_list = new_letters + new_numbers + new_symbols
    random.shuffle(new_list)
    password = "".join(new_list)
    if password_text.insert(0, password):
        pyperclip.copy(password)
    else:
        password_text.delete(0,END)
        password_text.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_details():
    website = website_text.get()
    user = username_text.get()
    password = password_text.get()
    new_data = {website: {
        "email": user,
        "password": password
    }}

    if len(password) == 0 or len(user) == 0 or len(website) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave any fields empty!")
    else:
        messagebox.showinfo(title="Success", message="Information was added successfully!")
        try:
            with open("entries.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("entries.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("entries.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_text.delete(0, END)
            username_text.delete(0,END)
            password_text.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50,)

canvas = Canvas(height=200, width=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

#Entries

website_text = Entry(width=21)
website_text.grid(row=1, column=1)

username_text = Entry(width=38)
username_text.grid(row=2, column=1, columnspan=2)

password_text = Entry(width=21, show="•")
password_text.grid(row=3, column=1)

#Labels

website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0)

username_label = Label(text="Email:", font=FONT)
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

#Buttons

generate_password = Button(text="Generate Password", cursor="hand2", command=generate_pw)
generate_password.grid(row=3, column=2)

add_pw = Button(text="Add", width=36, cursor="hand2", command=save_details)
add_pw.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", width=13, cursor="hand2", command=search_credentials)
search.grid(row=1, column=2)

window.mainloop()