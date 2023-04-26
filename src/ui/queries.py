from services.tk_service import TKService
from repositories.save_data import read_from_json as rfs

def choose_offset_account(self):
    accounts = [0, "Tulot", "Menot", "Oma tili", "Lainat"]
    print("Luokitellaan tilille tulevat tapahtumat.")
    print()
    for item in self.money_in.items():
        while True:
            print(f"Anna vastatatili tapahtumalle {item[0]}: {item[1]:.2f}.")
            offset = input("Vastatili (1: Tulot, 2: Menot, 3: Oma tili, 4: Lainat): ")
            if offset in ["1", "2", "3", "4"] and item[0] not in self.offset_account_in:
                self.offset_account_in[item[0]] = accounts[int(offset)]
                break
    print("Luokitellaan tililtä lähtevät tapahtumat.")
    print()
    for item in self.money_out.items():
        while True:
            print(f"Anna vastatatili tapahtumalle {item[0]}: {item[1]:.2f}.")
            offset = input("Vastatili (1: Tulot, 2: Menot, 3: Oma tili, 4: Lainat): ")
            if offset in ["1", "2", "3", "4"] and item[0] not in self.offset_account_out:
                if offset == "4":
                    while True:
                        interest = input("Anna korkojen määrä: ")
                        interest = interest.replace("-", "")
                        interest = interest.replace(",", ".")
                        interest = interest.replace("€", "")
                        if interest.replace(".", "").isdigit():
                            interest = round(float(interest), 2)
                            self.offset_account_out[item[0]] = accounts[int(offset)]
                            if item[0] not in self.interests:
                                self.interests[item[0]] = 0
                            self.interests[item [0]] += -interest
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

def search_events_by_one():
    print("Voit etsiä tapahtumia tallennetuilta tileiltä. Anna tili, jolta haluat hakea tietoja.")
    name = input("Tilin nimi: ")
    keys = ["Nimi", "Luokka"]
    print("Valittavissa olevat hakuavaimet ovat:")
    print(f" 1: {keys[0]}, 2: {keys[1]}")
    choice = input("Valintasi (numero + enter): ")
    key = keys[int(choice)-1]
    if key == "Nimi":
        print("Anna tapahtuman nimi, jolla haluat etsiä.")
        value = input("Tapahtuman nimi: ")
    rfs(name, key, value)
    