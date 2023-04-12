import tkinter as tk
from time import sleep


class StartGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("400x400")  # width x height
        self.root.title("Talouskatsaus")
        self.label = tk.Label(
            self.root, text="Käyttöohjeita tähän?", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)

        self.btn1 = tk.Button(self.buttonframe, text="Lisää tilitiedot", font=(
            'Arial', 18), pady=10, command=self.get_file)
        self.btn1.grid(row=0, column=1)
        self.btn2 = tk.Button(self.buttonframe, text="Siirry kyselyihin", font=(
            'Arial', 18), pady=10, command=self.make_queries)
        self.btn2.grid(row=1, column=1)
        self.btn3 = tk.Button(self.buttonframe, text="Lopeta", font=(
            'Arial', 18), pady=10, command=self.exit)
        self.btn3.grid(row=2, column=1)

        self.buttonframe.pack(fill='x')

        self.root.mainloop()

    def get_file(self):
        print("Siirrytään tilitietoihin")  # printtaa terminaaliin

    def make_queries(self):
        print("Siirrytään kyselyihin")  # printtaa terminaaliin

    def exit(self):
        print("Lopetetaan")  # printtaa terminaaliin
        sleep(0.5)
        exit()


StartGUI()
