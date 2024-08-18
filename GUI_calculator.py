import tkinter as tk

# Function to handle button clicks
def click_button(value):
    current = entry.get()
    if value == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for showing input and results
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Define button labels and their positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0, 4)  # C button spans across 4 columns
    ]

# Create and place buttons on the grid
for (text, row, column, colspan) in [(btn[0], btn[1], btn[2], btn[3] if len(btn) > 3 else 1) for btn in buttons]:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18), command=lambda t=text: click_button(t))
    button.grid(row=row, column=column, columnspan=colspan, sticky="nsew")

# Adjust column and row weights for proper resizing
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

# Run the Tkinter event loop
root.mainloop()
