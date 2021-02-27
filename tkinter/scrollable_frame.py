import tkinter as tk
from tkinter import ttk
'''
Implementation based on https://blog.tecladocode.com/tkinter-scrollable-frames/
'''


class ScrollableFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        canvas = tk.Canvas(self)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", tags="frame")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.bind('<Configure>', lambda e: canvas.itemconfig('frame', width=canvas.winfo_width()))


if __name__ == "__main__":

    class Demo(tk.Tk):
        def __init__(self):
            super().__init__()

            sf = ScrollableFrame(self)
            sf.pack(fill="both", expand=True)

            ROWS, COLS = 50, 10
            for col in range(COLS):
                sf.scrollable_frame.grid_columnconfigure(col, weight=1)
                for row in range(ROWS):
                    tk.Button(sf.scrollable_frame, text=f"Cell {row},{col}").grid(column=col, row=row, sticky="ew")

    root = Demo()
    root.mainloop()