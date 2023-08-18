from textblob import TextBlob
import tkinter as tk
from screeninfo import get_monitors

window = tk.Tk()
window.title("Spelling Checker")
window.config(bg="light blue")

input_label = tk.Label(window, text="Enter your input:", bg="light blue")
input_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

output_label = tk.Label(window, text="Output:", bg="light blue")
output_label.pack()

output_text = tk.Text(window, height=10, width=40)
output_text.pack()

def submit():
    input = input_entry.get()
    output_text.delete(1.0, tk.END)
    text_blob = TextBlob(input)
    output = text_blob.correct()
    output_text.insert(tk.END, output)
    output_text.config(fg="green")

submit_button = tk.Button(window, text="Submit", command=submit, fg="blue")
submit_button.pack()

screen_width = get_monitors()[0].width
screen_height = get_monitors()[0].height

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()

x = screen_width - window_width - 10
y = screen_height - window_height - 100

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()
