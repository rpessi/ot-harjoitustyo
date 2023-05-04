from services.tk_service import TKService
from repositories.save_data import read_from_json as rfj
from repositories.save_data import get_account_names
import cowsay
from services.reports import print_cash_report

def choose_offset_account(self):
    accounts = [0, "Tulot", "Menot", "Oma tili", "Lainat"]
    print(" Luokitellaan tilille tulevat tapahtumat. \n")
    for item in self.money_in.items():
        while True:
            print(f" Anna luokittelu tapahtumalle {item[0]}: {item[1]:.2f}.")
            offset = input(" Vastatili (1: Tulot, 2: Menot, 3: Oma tili, 4: Lainat): ")
            if offset in ["1", "2", "3", "4"] and item[0] not in self.offset_account_in:
                self.offset_account_in[item[0]] = accounts[int(offset)]
                break
    print(" Luokitellaan tililtä lähtevät tapahtumat. \n")
    for item in self.money_out.items():
        while True:
            print(f" Anna luokittelu tapahtumalle {item[0]}: {item[1]:.2f}.")
            offset = input(" Vastatili (1: Tulot, 2: Menot, 3: Oma tili, 4: Lainat): ")
            if offset in ["1", "2", "3", "4"] and item[0] not in self.offset_account_out:
                if offset == "4":
                    while True:
                        interest = input(" Anna korkojen määrä: ")
                        interest = interest.replace("-", "").replace(",", ".").replace("€", "")
                        if interest.isdigit():
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
                            print(" Anna korkojen määrä numeroina.")
                    break
                else:
                    self.offset_account_out[item[0]] = accounts[int(offset)]
                    break
    print(" Kaikki tapahtumat on luokiteltu.")

def search_events_by_name(): 
    accounts = get_account_names()
    if accounts == []: #tämä tilanne estetty toimintavalikon logiikan kautta
        print(" Tallennettuja tilejä ei löydy. Aloita tilitiedoston antamisella.")
        return
    options = list(range(1, len(accounts)+1))
    while True:
        cowsay.cow("Voit etsiä tapahtumia seuraavilta tileiltä:")
        for i in range(len(accounts)):
            print(f" {i+1}: {accounts[i]}")
        choice = input(" Valintasi: ")
        if choice.isdigit():
            if int(choice) in options:
                name = accounts[int(choice)-1]
                key = "Nimi"
                while True:
                    print(f" Valittu tili: {name} \n")
                    print(" Anna tapahtuman nimi (tai sen alku), jolla haluat etsiä.") #nääkin vois myöhemmin tarjota listana
                    value = input(" Tapahtuman nimi: ")
                    rfj(name, key, value)
                    next_choice = input(" Valitse: Uusi haku samalta tililtä (1) tai Takaisin päävalikkoon (2): ")
                    if next_choice == "1":
                        continue
                    else:
                        return
            else:
                print(" Valitse tarjolla olevista tileistä.")
                continue
        else:
            print(" Valitse annetuista tileistä. Käytä valintaan tilin numeroa.")
            continue

def choose_account_for_report(report_type):
    accounts = get_account_names()
    option = list(range(1, len(accounts)+1))
    while True:
        cowsay.cow("Voit tulostaa raportin seuraavilta tileiltä:")
        for i in range(len(accounts)):
            print(f" {i+1}: {accounts[i]}")
        choice = input(" Valintasi: ")
        if choice.isdigit():
            name = accounts[int(choice)-1]
            break
        else:
            print(" Valitse tili numerolla.")
    if report_type == "cash":
        print_cash_report(name)

