import tkinter as tk
from tkinter import scrolledtext

root=tk.Tk()
root.title("Christmas Wish List")
root.geometry("400x300")

def add_wish():
    wish=wish_entry.get()
    if wish:
        wish_list_box.insert(tk.END, wish)
        wish_entry.delete(0,tk.END)

#Entry widget to input a single line of text
wish_entry=tk.Entry(root, width=30) 
wish_entry.pack(pady=10)

#Button widget
add_button=tk.Button(root,text="Add a wish", command=add_wish)
add_button.pack(pady=10)

#Text widget for wish list
wish_list_box=scrolledtext.ScrolledText(root, width=40, height=10)
wish_list_box.pack(pady=10)

root.mainloop()