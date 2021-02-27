import tkinter as tk
from PIL import Image, ImageTk
'''
Basic image display in tkinter, with label.image attribute
used to mitigate garbage collection.
'''

root = tk.Tk()

image = ImageTk.PhotoImage(Image.open("image.png"))
label = tk.Label(root, image=image)
label.image = image
label.pack()

root.mainloop()