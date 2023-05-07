from rich import inspect
class TKService:

    def __init__(self, name):
        self.name = name
        self.money_in = {}
        self.money_out = {}
        self.balance = {}
        self.offset_account_in = {}
        self.offset_account_out = {}
        self.loans = {}
        self.interests = {}

    def summary(self, info):
        with open(info, "rt", encoding = "utf_8") as file:
            lines = file.readlines()
        for line in lines[1:]:
            line = line.split(";")
            amount = float(line[1].replace(",", "."))
            if amount < 0:
                if line[5] not in self.money_out:
                    self.money_out[line[5]] = 0
                self.money_out[line[5]] += amount
            else:
                if line[5] not in self.money_in:
                    self.money_in[line[5]] = 0
                self.money_in[line[5]] += float(amount)

    def print_cashflow(self, min_exp=100):
        total_misc_exp, total_money_in, total_money_out = (0, 0, 0,)
        print(f" Yhteenveto tilitapahtumista tililtä {self.name} \n Tilillepanot \n")
        for item in self.money_in.items():
            print(f" {item[0]}: {item[1]:.2f}")
            total_money_in += item[1]
        print("\n Tilisiirrot \n")
        for item in self.money_out.items():
            if abs(item[1]) < min_exp:
                total_misc_exp += item[1]
            else:
                print(f" {item[0]}: {-item[1]:.2f}")
                total_money_out += item[1]
        if total_misc_exp != 0:
            print(f" Muut tilisiirrot: {-total_misc_exp:.2f}")
        print(f"\n Panot yhteensä: {total_money_in:.2f} \n Nostot yhteensä: {-total_money_out:.2f}")
        return (total_money_in, total_money_out, total_misc_exp)

    def print_result(self, min_exp=100):
        total_misc_exp, total_income, total_expense = (0, 0, 0)
        print(f" Tuloslaskelma tililtä {self.name} \n Tulot \n")
        for item in self.money_in.items():
            if self.offset_account_in[item[0]] != "Lainat" and \
            self.offset_account_in[item[0]]!= "Oma tili":
                print(f" {item[0]}: {item[1]:.2f}")
                total_income += item[1]
        print("\n Menot \n")
        for item in self.money_out.items():
            if self.offset_account_out[item[0]] == "Lainat":
                payment = self.interests[item[0]]
                if abs(payment) < min_exp:
                    total_misc_exp += payment
                else:
                    print(f" {item[0]}: {-payment:.2f}")
                    total_expense += payment
            elif self.offset_account_out[item[0]] != "Oma tili":
                if abs(item[1]) < min_exp:
                    total_misc_exp += item[1]
                else:
                    print(f" {item[0]}: {-item[1]:.2f}")
                    total_expense += item[1]
        if total_misc_exp != 0:
            print(f" Muut menot: {-total_misc_exp:.2f}")
        print(f"\n Tulot yhteensä: {total_income:.2f} \n Menot yhteensä: {-total_expense:.2f}")
        return (total_income, total_expense, total_misc_exp)
