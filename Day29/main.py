from tkinter import *
from tkinter import messagebox

# Constants
BACKGROUND = "#120321"
FONT_NAME = "Courier"

# Creating the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20, bg=BACKGROUND)
window.resizable(False,False)

# ========================= Taking the file ==================
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) != 0 and len(username) != 0 and len(password) != 0:
        response = messagebox.askokcancel(
            title="Save",
            message=(
                "These are the details you entered:\n"
                f"Website: {website}\n"
                f"Email: {username}\n"
                f"Password: {password}\n"
                "Save to file?"
            )
        )
        if response:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title="Error", message="Don't leave any place empty")

# ========================= UI SETUP =========================

# Canvas with logo
logo = PhotoImage(file='logo.png')
canvas = Canvas(width=logo.width(), height=logo.height(), bg=BACKGROUND, highlightthickness=0)
canvas.create_image(logo.width() // 2, logo.height() // 2, image=logo)
canvas.grid(row=0, column=1)

# Website
website_label = Label(text="Website:", bg=BACKGROUND, fg="white", font=(FONT_NAME, 12))
website_label.grid(row=1, column=0, sticky="e")
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()

# Email/Username
username_label = Label(text="Email/Username:", bg=BACKGROUND, fg="white", font=(FONT_NAME, 12))
username_label.grid(row=2, column=0, sticky="e")
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
username_entry.insert(0, "abnzr@gmail.com")

# Password
password_label = Label(text="Password:", bg=BACKGROUND, fg="white", font=(FONT_NAME, 12))
password_label.grid(row=3, column=0, sticky="e")
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1, sticky="w")
gen_pwd = Button(text="Generate Password", width=21, bg=BACKGROUND, fg="white", font=(FONT_NAME, 10))
gen_pwd.grid(row=3, column=2, sticky="ew")

# Add Button
add_button = Button(
    text="Add",
    width=36,
    bg=BACKGROUND,
    fg="white",
    font=(FONT_NAME, 10),
    command=save_password
)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")



window.mainloop()
