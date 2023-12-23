import tkinter as tk

root = tk.Tk()
root.title("Christmas Wish List")
root.geometry("400x400")

# Function to add a wish
def add_wish():
    wish = wish_entry.get()
    if wish:  # Check if the wish is not empty
        var = tk.BooleanVar()  # BooleanVar to track the Checkbutton state
        chk = tk.Checkbutton(wish_frame_interior, text=wish, variable=var)  # Create Checkbutton for each wish
        chk.pack(anchor='w')  # Align to the west (left side)
        wish_entry.delete(0, tk.END)  # Clear the entry widget for new entry

# Entry widget for wish input
wish_entry = tk.Entry(root, width=30)
wish_entry.pack(pady=10)

# Button to add a wish
add_button = tk.Button(root, text="Add Wish", command=add_wish)
add_button.pack(pady=5)

# Canvas and Scrollbar setup
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Frame for Checkbuttons inside the Canvas
wish_frame_interior = tk.Frame(canvas)
canvas.create_window((0, 0), window=wish_frame_interior, anchor="nw")

def _configure_interior(event):
    # Update the scrollregion to encompass the inner frame
    size = (wish_frame_interior.winfo_reqwidth(), wish_frame_interior.winfo_reqheight())
    canvas.config(scrollregion="0 0 %s %s" % size)

def _configure_canvas(event):
    if wish_frame_interior.winfo_reqwidth() != canvas.winfo_width():
        # Update the inner frame's width to fill the canvas
        canvas.itemconfigure(wish_frame_interior_id, width=canvas.winfo_width())

wish_frame_interior.bind('<Configure>', _configure_interior)
canvas.bind('<Configure>', _configure_canvas)

# Start the GUI
root.mainloop()
