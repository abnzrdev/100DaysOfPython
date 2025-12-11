from tkinter import *
import requests

def get_quote():
    try:
        res = requests.get("https://api.kanye.rest/", timeout=5)
        res.raise_for_status()
        quote = res.json().get("quote", "No quote found.")
    except Exception:
        quote = "Kanye will talk later"
    return quote

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)
window.resizable(False, False)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote = get_quote()
quote_text = canvas.create_text(150, 207, text=quote, width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()