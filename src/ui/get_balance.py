import tkinter as tk
from tkinter import ttk

#under construction

root = tk.Tk()
root.geometry("300x100")
root.title("Anna tilin alkusaldo")
balance = tk.StringVar()


balance_entry = ttk.Entry(root, textvariable = balance)
balance_entry.pack(fill="x")
balance_entry.focus()

def entry_clicked():
    print(f"{balance}")
    return(balance)
    
    

entry_button = ttk.Button(root, text = "OK", command = entry_clicked)
entry_button.pack(fill="x", pady=20, padx=50)

root.mainloop()




if __name__ == "__main__":
    pass
