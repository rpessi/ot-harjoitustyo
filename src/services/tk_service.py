#jotain importteja?

class TKService:

    def __init__(self, name):
        self.name = name
        self.income = {}
        self.expense = {}
        self.total_misc_exp = 0
        self.total_income = 0
        self.total_expense = 0

    #tää on vähän kertakäyttöisessä asennossa vielä
    def summary(self, data):  #3. viikon tilapäistoiminto testauksia varten, Nordean tiliote
        with open(data) as file:
            lines = file.readlines()
        for line in lines[1:]: #skipataan otsikkorivi
            date, amount, a, b, c, name, e, f = line.split(";")
            amount = float(amount.replace(",", "."))
            if amount < 0: 
                if name not in self.expense:
                    self.expense[name] = 0
                self.expense[name] += -amount #lisätään menoihin plusmerkkisenä
            else:
                if name not in self.income:
                    self.income[name] = 0
                self.income[name] += float(amount)

        return ((self.income, self.expense)) #tarviiko ees palauttaa mitään?
    
    def print_summary(self, min=100):
        self.total_misc_exp = 0
        print("Tulot")
        print()
        for key in self.income:
            print(f"{key}: {self.income[key]:.2f}")
            self.total_income += self.income[key]
        print()
        print("Menot")
        print()
        for key in self.expense:
            if self.expense[key] < min:
                self.total_misc_exp += self.expense[key]
                print(f"Lisättiin sekalaisiin {key} : {self.expense[key]}")
            else:
                print(f"{key}: {self.expense[key]:.2f}")
            self.total_expense += self.expense[key]
        print(f"Muut menot: {self.total_misc_exp:.2f}")
        print()
        print(f"Tulot yhteensä: {self.total_income:.2f}")
        print(f"Menot yhteensä: {self.total_expense:.2f}")

if __name__ == "__main__":
    tili = TKService("Nordea")
    data = "/home/rpessi/ohte/src/tests/test_file.csv"
    sum_up = tili.summary(data)
    tili.print_summary()
    tili.print_summary(min=200)

