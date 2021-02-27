import tkinter as tk
from tkinter import ttk


class ScrollableColumn(tk.Canvas):
    '''
    A single scrollable column of widgets
    '''
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self._scrollable_frame = ttk.Frame(self)
        self._scrollable_frame.bind("<Configure>", lambda e: self.configure(scrollregion=self.bbox("all")))
        self._scrollable_frame.columnconfigure(0, weight=1)

        self.create_window((0, 0), window=self._scrollable_frame, anchor="nw", tags="frame")
        self.configure(yscrollcommand=self.master._scrollbar.set)
        self.bind('<Configure>', lambda e: self.itemconfig('frame', width=self.winfo_width()))


class Column:
    '''
    A logical grouping of a heading label and ScrollableColumn instance
    '''
    def __init__(self, master, index, heading):
        self.master = master
        self.index = index

        self._heading = tk.StringVar(value=heading)
        self._heading_label = ttk.Label(self.master, textvariable=self._heading, anchor="center")
        self._heading_label.grid(row=0, column=self.index, sticky="news")

        self._scrollable_column = ScrollableColumn(self.master)
        self._scrollable_column.grid(row=1, column=self.index, sticky="news")

        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(self.index, weight=1)


class ScrollableTable(ttk.Frame):
    '''
    Multiple ScrollableColumns are attached to a single scrollbar.
    '''
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self._columns = []

        self._scrollbar = ttk.Scrollbar(self, orient="vertical", command=self._yview)
        self._scrollbar.grid(row=1, column=0, sticky="nse")

    @classmethod
    def from_headings(cls, master, headings):
        table = cls(master)
        for heading in headings:
            table.add_column(heading)
        return table

    @property
    def _next_column_index(self):
        return len(self._columns)

    def _yview(self, *args):
        for column in self._columns:
            column._scrollable_column.yview(*args)

    def add_column(self, heading):
        self._columns.append(Column(self, self._next_column_index, heading))
        self._scrollbar.grid(row=1, column=self._next_column_index + 1, sticky="nse")
        self.columnconfigure(self._next_column_index + 1, weight=0)

    def add_widget(self, column, row, widget, *args, **kwargs):
        new_widget = widget(self._columns[column]._scrollable_column._scrollable_frame, *args, **kwargs)
        new_widget.grid(column=0, row=row, sticky="ew")


if __name__ == "__main__":

    class Demo(tk.Tk):
        def __init__(self):
            super().__init__()

            COLS, ROWS = 5, 50
            headings = [f"Column {col}" for col in range(COLS)]

            table = ScrollableTable.from_headings(self, headings)
            table.pack(fill="both", expand=True)

            for col in range(COLS):
                for row in range(ROWS):
                    table.add_widget(col, row, ttk.Button, text=f"{col}, {row}")

    root = Demo()
    root.mainloop()