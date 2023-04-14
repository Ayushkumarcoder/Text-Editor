import tkinter as tk
window = tk.Tk()
window.title("Text Converter")

# crating the grid
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# crating the four widgets that we need

frame = tk.Frame(master=window, relief=tk.RAISED, bd=2)
text = tk.Text(window)
open_button = tk.Button(frame, text="Open")
save_button = tk.Button(frame, text="Save the file")


# creating the grid

open_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
save_button.grid(row=1, column=0, sticky="ew", padx=5)

frame.grid(row=0, column=0, sticky="ns")
text.grid(row=0, column=1, sticky="nsew")











window.mainloop()