import tkinter as tk

root = tk.Tk()

frame1 = tk.LabelFrame(root, text="Frame 1", bg="blue", fg="white")
frame1.grid(row=0, column=0, sticky="news")
button1 = tk.Button(frame1, text="Switch to Frame 2", command=lambda: frame2.lift())
button1.pack(padx=20, pady=20, fill="both", expand=True)

frame2 = tk.LabelFrame(root, text="Frame 2", bg="orange", fg="black")
frame2.grid(row=0, column=0, sticky="news")
button2 = tk.Button(frame2, text="Switch to Frame 1", command=lambda: frame1.lift())
button2.pack(padx=20, pady=20, fill="both", expand=True)

frame1.lift()

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()