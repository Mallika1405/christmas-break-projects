import tkinter as tk

root = tk.Tk()
root.title("Christmas Wish List")
root.geometry("400x400")

# Function to add a wish
def add_wish():
    wish = wish_entry.get()
    if wish:  # Check if the wish is not empty
        var = tk.BooleanVar()  # BooleanVar to track the Checkbutton state
        chk = tk.Checkbutton(wish_frame, text=wish, variable=var)  # Create Checkbutton for each wish
        chk.pack(anchor='w')  # Align to the west (left side)
        wish_entry.delete(0, tk.END)  # Clear the entry widget for new entry

# Entry widget for wish input
wish_entry = tk.Entry(root, width=30)
wish_entry.pack(pady=10)

# Button to add a wish
add_button = tk.Button(root, text="Add Wish", command=add_wish)
add_button.pack(pady=5)

# Frame for CheckButtons
wish_frame = tk.Frame(root)
wish_frame.pack(pady=10)

# Adding a scrollbar
scrollbar = tk.Scrollbar(wish_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Start the GUI
root.mainloop()
