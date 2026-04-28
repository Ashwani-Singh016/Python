#drpdown
from  tkinter import *
import tkinter as tk

root=Tk()
menu=["Rohit","Harsh","Ashwani","Devesh","Raj","Varun","Tanishq","Utkarsh"]
variable=StringVar(root)
variable.set("choose")
	
drop1=OptionMenu(root,variable,*menu)
drop1.pack()
root.geometry("400x500")

#update dropdown

def update_dropdown():
    # Clear old options
    menu = dropdown["menu"]
    menu.delete(0, "end")

    # Add new options dynamically
    new_options = ["Python", "C++", "Java", "Rust"]
    for option in new_options:
        menu.add_command(label=option, command=lambda value=option: selected.set(value))

root = tk.Tk()
root.title("Dropdown Modification Example")

selected = tk.StringVar(value="Select Language")

# Initial dropdown
options = ["HTML", "CSS", "JavaScript"]
dropdown = tk.OptionMenu(root, selected, *options)
dropdown.pack(pady=10)

# Button to modify dropdown
btn = tk.Button(root, text="Update Dropdown", command=update_dropdown)
btn.pack(pady=10)

root.mainloop()
root.mainloop()