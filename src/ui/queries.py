from services.tk_service import TKService
from repositories.save_data import read_from_json as rfj
from repositories.save_data import get_account_names
import cowsay
from ui.reports import print_cash_report
from rich.console import Console
from rich.prompt import Prompt

def choose_offset_account(self):
    console = Console()
    accounts = [0, "Tulot", "Menot", "Oma tili", "Lainat"]
    console.print(" Luokitellaan tilille tulevat tapahtumat. \n")
    for item in self.money_in.items():
        while True:
            console.print(f" Anna luokittelu tapahtumalle {item[0]}: {item[1]:.2f}.")
            offset = input(" Vastatili (1: Tulot, 2: Menot, 3: Oma tili, 4: Lainat): ")
            if offset in ["1", "2", "3", "4"] and item[0] not in self.offset_account_in:
                self.offset_account_in[item[0]] = accounts[int(offset)]
                break
    console.print(" Luokitellaan tililtä lähtevät tapahtumat. \n")
    for item in self.money_out.items():
        while True:
            console.print(f" Anna luokittelu tapahtumalle {item[0]}: {item[1]:.2f}.")
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
                            console.print(" Anna korkojen määrä numeroina.", style = 'dark red')
                    break
                else:
                    self.offset_account_out[item[0]] = accounts[int(offset)]
                    break
    console.print(" Kaikki tapahtumat on luokiteltu.", style = 'green')

def search_events_by_name(): 
    console = Console()
    accounts = get_account_names()
    if accounts == []: #tämä tilanne estetty toimintavalikon logiikan kautta
        console.print(" Tallennettuja tilejä ei löydy. Aloita tilitiedoston antamisella.", style = 'dark red')
        return
    cowsay.cow("Valitse tili, jolta haluat etsiä tapahtumia!")
    name = Prompt.ask(" Valintasi ", choices = accounts)
    key = "Nimi"
    while True:
        console.print(f" Valittu tili: {name} \n", style = 'blue')
        console.print(" Anna tapahtuman nimi (tai sen alku), jolla haluat etsiä.", style= 'blue') #nääkin vois myöhemmin tarjota listana
        value = Prompt.ask(" Tapahtuman nimi: ")
        rfj(name, key, value)
        next_choice = Prompt.ask(" Valitse: Uusi haku samalta tililtä (1) tai Takaisin päävalikkoon (2): ")
        if next_choice == "1":
            continue
        else:
            return

def choose_account_for_report(report_type):
    console = Console()
    accounts = get_account_names()
    cowsay.cow("Valitse tili, jolta haluat raportin!")
    choice = Prompt.ask(" Valintasi ", choices = accounts)
    if report_type == "cash":
        print_cash_report(choice)
