import tkinter as tk
'''
Allowing widgets to expand into free space using the 
pack and grid geometry managers.
'''

root = tk.Tk()

left_frame = tk.Frame(root)
left_frame.pack(side="left", fill="both", expand=True)
right_frame = tk.Frame(root)
right_frame.pack(side="left", fill="both", expand=True)

# Using pack
left_button = tk.Button(left_frame, text="Button.pack()")
left_button.pack(fill="both", expand=True, padx=10, pady=10)

# Using grid
right_button = tk.Button(right_frame, text="Button.grid()")
right_button.grid(row=0, column=0, sticky="news", padx=10, pady=10)
right_frame.grid_columnconfigure(0, weight=1)
right_frame.grid_rowconfigure(0, weight=1)

root.mainloop()