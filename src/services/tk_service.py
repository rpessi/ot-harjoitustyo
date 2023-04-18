# jotain importteja?

class TKService:

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.money_in = {} #cash flow
        self.money_out = {} #cash flow
        self.balance = {}
        self.offset_account_in = {} #vastatilit panoille / tilitapahtumien luokittelu
        self.offset_account_out = {} #vastatilit otoille / tilitapahtumien luokittelu

    # cashflow, tää on vähän kertakäyttöisessä asennossa vielä
    def summary(self, info):  # 3. viikon tilapäistoiminto testauksia varten, Nordean tiliote
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

    def print_summary(self, min_exp=100): #tilitapahtumat/kassavirta
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
        return total_misc_exp
