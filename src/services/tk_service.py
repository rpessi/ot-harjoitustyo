#jotain importteja?
class TKService:

    def __init__(self, name, path): #path on jo absoluuttinen polku
        self.name = name
        self.path = path
        self.money_in = {} #cash flow
        self.money_out = {} #cash flow
        self.balance = {}
        self.offset_account_in = {} #vastatilit panoille / tilitapahtumien luokittelu
        self.offset_account_out = {} #vastatilit otoille / tilitapahtumien luokittelu
        self.loans = {} #lainojen hoitokulut, kokonaismäärä
        self.splits = {} #lainojen korot, kokonaismäärä

    # cashflow, toimii myös tilitapahtumien luokittelun apuna
    def summary(self, info):
        with open(info, "rt", encoding = "utf_8") as file:
            lines = file.readlines()
        for line in lines[1:]:  # skipataan otsikkorivi
            line = line.split(";")
            # date = line_list[0] #ei ole tässä vaiheessa vielä käytössä
            amount = float(line[1].replace(",", "."))
            if amount < 0:
                if line[5] not in self.money_out:
                    self.money_out[line[5]] = 0
                # lisätään menoihin miinusmerkkisenä
                self.money_out[line[5]] += amount
            else:
                if line[5] not in self.money_in:
                    self.money_in[line[5]] = 0
                self.money_in[line[5]] += float(amount)

    #tilitapahtumat/kassavirta, ei perustu vielä pysyväistallennukseen
    def print_cashflow(self, min_exp=100):
        total_misc_exp = 0
        total_money_in = 0
        total_money_out = 0
        print(f"Yhteenveto tilitapahtumista tililtä {self.name}")
        print()
        print("Tilillepanot")
        print()
        for item in self.money_in.items():
            print(f"{item[0]}: {item[1]:.2f}")
            total_money_in += item[1]
        print()
        print("Tilisiirrot")
        print()
        for item in self.money_out.items():
            if abs(item[1]) < min_exp:
                total_misc_exp += item[1]
            else:
                print(f"{item[0]}: {-item[1]:.2f}") #printataan plusmerkkisenä
                total_money_out += item[1]
        print(f"Muut tilisiirrot: {-total_misc_exp:.2f}")
        print()
        print(f"Panot yhteensä: {total_money_in:.2f}")
        print(f"Nostot yhteensä: {-total_money_out:.2f}")
        return (total_money_in, total_money_out, total_misc_exp) #palautukset testejä varten
    #tuloslaskelma
    def print_result(self, min_exp=100):
        total_misc_exp = 0
        total_income = 0
        total_expense = 0
        print(f"Tuloslaskelma tililtä {self.name}")
        print()
        print("Tulot")
        print()
        for item in self.money_in.items(): #skipataan lainat ja tilisiirrot omien tilien välillä
            if self.offset_account_in[item[0]] != "Lainat" and self.offset_account_in[item[0]] != "Oma tili":
                print(f"{item[0]}: {item[1]:.2f}")
                total_income += item[1]
        print()
        print("Menot")
        print()
        for item in self.money_out.items():
            if self.offset_account_out[item[0]] == "Lainat":
                payment = self.splits[item[0]] #korkojen osuus
                if abs(payment) < min_exp:
                    total_misc_exp += payment
                else:
                    print(f"{item[0]}: {-payment:.2f}") #printataan plusmerkkisenä
                    total_expense += payment
            elif self.offset_account_out[item[0]] != "Oma tili":
                if abs(item[1]) < min_exp:
                    total_misc_exp += item[1]
                else:
                    print(f"{item[0]}: {-item[1]:.2f}") #printataan plusmerkkisenä
                    total_expense += item[1]
        print(f"Muut menot: {-total_misc_exp:.2f}")
        print()
        print(f"Tulot yhteensä: {total_income:.2f}")
        print(f"Menot yhteensä: {-total_expense:.2f}")
        return (total_income, total_expense, total_misc_exp) #palautukset testejä varten
