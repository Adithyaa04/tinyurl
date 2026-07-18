import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("URL Shortener")
root.config(bg="#7AD2A7")

url = StringVar()
ur_address = StringVar()



def shorten_url():
    url_address = url.get()
    if url_address:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url_address)
        ur_address.set(short_url)
        pyperclip.copy(short_url)
        result_label.config(text=f"Shortened URL: {short_url}\nCopied to clipboard!")
    else:
        result_label.config(text="Please enter a valid URL.")


def copy_to_clipboard():
    if ur_address.get():
        pyperclip.copy(ur_address.get())
        result_label.config(text=f"Copied: {ur_address.get()}")



url_label = Label(root, text="Enter URL:", font=("Arial", 12), bg="#7AD2A7")
url_label.pack(pady=10)

url_entry = Entry(root, textvariable=url, font=("Arial", 12), width=30)
url_entry.pack(pady=10)

shorten_button = Button(root, text="Shorten URL", font=("Arial", 12), bg="#5DADE2", command=shorten_url)
shorten_button.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 12), bg="#7AD2A7")
result_label.pack(pady=10)

result_entry = Entry(root, textvariable=ur_address, font=("Arial", 12), width=30)
result_entry.pack(pady=10)

copy_button = Button(root, text="Copy to Clipboard", font=("Arial", 12), bg="#5DADE2", command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()