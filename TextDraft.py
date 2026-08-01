import tkinter as tk
from tkinter import filedialog , messagebox

# structure of main text editor
root = tk.Tk()
root.title("TextDraft")
root.geometry("600x500")

# text part
text = tk.Text(
    root,
    wrap = tk.WORD,
    font = ("Italic",12)
)

text.pack(expand = True , fill = tk.BOTH)

# function 1- create  new file

def new_file():
    text.delete(1.0, tk.END)

# function 2 - open a file

def open_file():
    # open a file
    file_path = filedialog.askopenfilename(
        defaultextension= ".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# function 3 - save the file
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension= ".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

    messagebox.showinfo("Info", "File Saved Successfully!")

# create menu bar
menu = tk.Menu(root)
root.config(menu = menu)
file_menu = tk.Menu(menu)

# options in menu bar 
menu.add_cascade(label="File", menu=file_menu)

# create options in file in main menu bar
file_menu.add_command(label="New", command= new_file)
file_menu.add_command(label="Open", command= open_file)
file_menu.add_command(label="Save", command= save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

     

# start and generate structre as output
root.mainloop()
