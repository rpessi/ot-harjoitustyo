from services.tk_service import TKService

def choose_offset_account(self): #valitaan tilitapahtumille vastatilit
    accounts = [0, "Tulot", "Menot", "Oma tili", "Lainat"]
    print("Luokitellaan tilille tulevat tapahtumat.")
    print("Voit kirjata menoihin esim. irtaimiston myynnit.")
    print()
    for item in self.money_in.items():
        while True: #mieti uusiksi tilanteessa, kun aiempia tapahtumia on jo luokiteltu
            print(f"Anna vastatatili tapahtumalle {item[0]}: {item[1]:.2f}.")
            offset = input("Vastatili (1: Tulot, 2: Menot, 3: Oma tili, 4: Lainat): ")
            if offset in ["1", "2", "3", "4"] and item[0] not in self.offset_account_in:
                self.offset_account_in[item[0]] = accounts[int(offset)]
                break
    print("Luokitellaan tililtä lähtevät tapahtumat.")
    print("Voit kirjata tuloihin esim. jälkiverot.")
    print()
    for item in self.money_out.items():
        while True: #mieti uusiksi tilanteessa, kun aiempia tapahtumia on jo luokiteltu
            print(f"Anna vastatatili tapahtumalle {item[0]}: {item[1]:.2f}.") #item[1] on jo float
            offset = input("Vastatili (1: Tulot, 2: Menot, 3: Oma tili, 4: Lainat): ")
            if offset in ["1", "2", "3", "4"] and item[0] not in self.offset_account_out:
                if offset == "4":
                    while True:
                        interest = input("Anna korkojen määrä: ")
                        interest = interest.replace("-", "")
                        interest = interest.replace(",", ".")
                        interest = interest.replace("€", "")
                        if interest.replace(".", "").isdigit():
                            interest = float(interest)
                            self.offset_account_out[item[0]] = accounts[int(offset)]
                            if item[0] not in self.splits:
                                self.splits[item[0]] = 0
                            self.splits[item [0]] += -interest
                            if item[0] not in self.loans:
                                self.loans[item[0]] = 0
                            self.loans[item[0]] += item[1]
                            break
                        else:
                            print("Anna korkojen määrä numeroina.")
                    break
                else:
                    self.offset_account_out[item[0]] = accounts[int(offset)]
                    break
    print("Kaikki tapahtumat on luokiteltu.")
    #print("splits", self.splits)
    #print("offset_in", self.offset_account_in)
    #print("offset_out", self.offset_account_out)
    #print("lainat", self.loans)
#lainatapahtumien pilkkominen

#menoluokkien tarkennus

#opening balances