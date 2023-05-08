"Käyttöliittymää tukeva osio, joka sisältää kyselyjä"

from services.tk_service import TKService
from repositories.save_data import read_from_json as rfj
from repositories.save_data import get_account_names
import cowsay
from ui.reports import print_account_report, print_success
from rich.console import Console
from rich.prompt import Prompt

def choose_offset_account(self:TKService):
    """Pyytää käyttäjää luokittelemaan tilitapahtumat
    
        Args: TKService()-instanssi
    """
    console = Console()
    accounts = [0, "Tulot", "Menot", "Oma tili", "Lainat"]
    console.print(" Luokitellaan tilille tulevat tapahtumat. \n")
    for item in self.money_in.items():
        while True:
            console.print(f" Anna luokittelu tapahtumalle {item[0]}: {item[1]:.2f}.")
            console.print(" Vastatilit: 1: Tulot, 2: Menot, 3: Oma tili, 4: Lainat")
            offset = int(Prompt.ask("Valintasi", choices = ["1", "2", "3", "4"]))
            if item[0] not in self.offset_account_in:
                self.offset_account_in[item[0]] = accounts[offset]
                break
    console.print(" Luokitellaan tililtä lähtevät tapahtumat. \n")
    for item in self.money_out.items():
        while True:
            console.print(f" Anna luokittelu tapahtumalle {item[0]}: {item[1]:.2f}.")
            console.print(" Vastatilit: 1: Tulot, 2: Menot, 3: Oma tili, 4: Lainat")
            offset = int(Prompt.ask("Valintasi", choices = ["1", "2", "3", "4"]))
            if item[0] not in self.offset_account_out:
                if offset == 4:
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
    print_success("Tilitapahtumien luokittelu")

def search_events_by_name(): 
    """Toiminto tilitapahtumien hakemista varten"""
    console = Console()
    accounts = get_account_names()
    if not accounts:
        console.print(" Tallennettuja tilejä ei löydy. Aloita tilitiedoston antamisella.", style = 'dark red')
        return
    cowsay.cow("Valitse tili, jolta haluat etsiä tapahtumia!")
    name = Prompt.ask(" Valintasi ", choices = accounts)
    key = "Nimi"
    while True:
        console.print(f" Valittu tili: {name} \n", style = 'blue')
        console.print(" Anna tapahtuman nimi (tai sen alku), jolla haluat etsiä.", style= 'blue')
        value = Prompt.ask(" Tapahtuman nimi: ")
        rfj(name, key, value)
        next_choice = Prompt.ask(" Valitse: Uusi haku samalta tililtä (1) tai Takaisin päävalikkoon (2): ")
        if next_choice == "1":
            continue
        else:
            return

def choose_account_for_report():
    """Toiminto raporttien tulostukseen, joka pyytää käyttäjän valitsemaan tilin, jolta raportti tulostetaan,
        sekä raporttityypin."""
    console = Console()
    accounts = get_account_names()
    cowsay.cow("Valitse tili, jolta haluat raportin!")
    name = Prompt.ask(" Valintasi ", choices = accounts)
    console.print(" Valitse raporttityyppi: 1: Tuloslaskelma, 2: Kassavirtalaskelma, 3: Muutokset taseessa")
    report_type = Prompt.ask("Valitse raportin tyyppi", choices = ["1", "2", "3"])
    print_account_report(name, int(report_type))
