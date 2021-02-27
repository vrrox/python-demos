import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    app = App()
    app.mainloop()