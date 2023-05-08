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
