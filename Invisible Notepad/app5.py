import tkinter as tk

root = tk.Tk()
root.wm_attributes('-transparentcolor', '#add123')
root.config(bg='#add123')

text = tk.Text(root, bg='#add123', width=170, height=50)
text.insert(tk.END, 'This is a test message')
text.pack()
text.configure(font=('Times New Roman', 12,))

root.attributes('-fullscreen', True)

root.mainloop()
