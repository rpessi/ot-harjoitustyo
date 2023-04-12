# jotain importteja?

class TKService:

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.income = {}
        self.expense = {}
        #self.total_misc_exp = 0 #onko turhat täällä?
        #self.total_income = 0 #onko turhat täällä?
        #self.total_expense = 0 #onko turhat täällä?
        self.offset_account_in = {} #vastatilit panoille
        self.offset_account_out = {} #vastatilit otoille
        print("tultiin TKServicen inittiin")

    # tää on vähän kertakäyttöisessä asennossa vielä
    def summary(self, info):  # 3. viikon tilapäistoiminto testauksia varten, Nordean tiliote
        with open(info, "rt", encoding = "utf_8") as file:
            lines = file.readlines()
        for line in lines[1:]:  # skipataan otsikkorivi
            line_list = line.split(";")
            # date = line_list[0] #ei ole tässä vaiheessa vielä käytössä
            amount = float(line_list[1].replace(",", "."))
            name = line_list[5]
            if amount < 0:
                if name not in self.expense:
                    self.expense[name] = 0
                # lisätään menoihin miinusmerkkisenä
                self.expense[name] += amount
            else:
                if name not in self.income:
                    self.income[name] = 0
                self.income[name] += float(amount)
        print("päästiin summaryn loppuun")

    def print_summary(self, min_exp=100):
        self.total_misc_exp = 0
        self.total_income = 0
        self.total_expense = 0
        print()
        print(f"Yhteenveto tililtä {self.name}")
        print()
        print("Tulot")
        print()
        for item in self.income.items():
            print(f"{item[0]}: {item[1]:.2f}")
            self.total_income += item[1]
        print()
        print("Menot")
        print()
        for item in self.expense.items():
            if abs(item[1]) < min_exp:
                self.total_misc_exp += item[1]
                # print(f"Lisättiin sekalaisiin {item[0]} : {item[1]}")
            else:
                print(f"{item[0]}: {-item[1]:.2f}") #printataan plusmerkkisenä
            self.total_expense += item[1]
        print(f"Muut menot: {-self.total_misc_exp:.2f}")
        print()
        print(f"Tulot yhteensä: {self.total_income:.2f}")
        print(f"Menot yhteensä: {-self.total_expense:.2f}")
        print()

    

#lainatapahtumien pilkkominen

#menoluokkien tarkennus

#opening balances 

if __name__ == "__main__":
    tili = TKService("Nordea")
    DATA = "/home/rpessi/ohte/src/tests/test_file.csv"
    sum_up = tili.summary(DATA)
    tili.print_summary()
    tili.print_summary(min_exp=200)
    #tili.choose_offset_account()

