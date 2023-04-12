import tkinter as tk
from tkinter import filedialog as fd
from time import sleep
import get_balance


class FilesGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.opening_balance = 0

        self.root.geometry("400x400")  # width x height
        self.root.title("Talouskatsaus")
        self.label = tk.Label(
            self.root, text="Valitse talletettava CSV-tiedosto", font=('Arial', 18))
        self.label.pack(padx=20, pady=20)

        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

        self.btn1 = tk.Button(self.buttonframe, text="Valitse CSV-tiedosto",
                              font=('Arial', 18), pady=10, command=self.select_file)
        self.btn1.grid(row=0, column=1)
        self.btn2 = tk.Button(self.buttonframe, text="Siirry kyselyihin", font=(
            'Arial', 18), pady=10, command=self.make_queries)
        self.btn2.grid(row=1, column=1)
        self.btn3 = tk.Button(self.buttonframe, text="Lopeta", font=(
            'Arial', 18), pady=10, command=self.exit)
        self.btn3.grid(row=2, column=1)

        self.buttonframe.pack(fill='x')

        self.root.mainloop()

    def select_file(self):
        # self.filetypes = (('csv files', '*.csv')), en saanu tätä toimimaan
        self.file = fd.askopenfilename(
            initialdir="/home", title="Valitse CSV-tiedosto")
        # luettavan tiedoston osoite
        #tässä pyydetään antamaan tilille nimi
        #lisäksi pyydetään alkusaldoa
        if self.opening_balance == 0:
            self.opening_balance = get_balance.entry_clicked()
        #self.opening_balance = tk.Entry(self, width = 50)
        #self.opening_balance.pack()
        #print("Otettiin vastaan tiedosto", self.file)

    def make_queries(self):
        print("Siirrytään kyselyihin")

    def exit(self):
        print("Lopetetaan")
        sleep(0.5)
        exit()


FilesGUI()
