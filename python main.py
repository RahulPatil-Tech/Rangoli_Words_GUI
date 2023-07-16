import tkinter as tk
import tkinter.messagebox as messagebox
import string
from tkinter.ttk import Combobox

root = tk.Tk()
root.title("Rangoli Words")
root.geometry("190x190")

def print_rangoli():
    size = int(combobox.get())
    alpha = string.ascii_lowercase
    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
    rangoli_output = '\n'.join(L[:0:-1] + L)
    messagebox.showinfo("Rangoli Output", rangoli_output)

size_label = tk.Label(root, text="Number of words in rangoli:")
size_label.pack()

size_values = [str(i) for i in range(1, 27)]  
combobox = Combobox(root, values=size_values)
combobox.pack()

button = tk.Button(root, text="Print Rangoli", command=print_rangoli)
button.pack()

root.mainloop()
