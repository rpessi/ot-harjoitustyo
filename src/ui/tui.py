"""Osio, joka sisältää käyttöliittymän"""

from services.tk_service import TKService
import cowsay
import ui.queries
from ui.reports import print_success
import repositories.save_data
from repositories.save_data import get_account_names, convert_from_s_pankki
from rich.console import Console
from rich.prompt import Prompt

def get_file(file_type: str):
    """Pyytää käyttäjältä tallennettavan tiedoston ja pyytää käyttäjää antamaan tilille nimen

    Returns:
        Tuple, jossa on tiedoston nimi ja polku yhdistettynä, sekä käyttäjän tilille antama nimi
    """
    while True:
        file = input( " Anna csv-tiedoston nimi ja polku: ")
        if check_file(file):
            name = input(" Anna tilin nimi: ")
            if file_type == "Nordea":
                newfile = file
            if file_type == "S-Pankki":
                newfile = convert_from_s_pankki(file)
                print_success("S-Pankin tiliotteen muokkaus")
            break
        else:
            print(" Tiedostoa ei löydy tai se ei ole csv-tiedosto.")
    return((newfile, name))

def check_file(file:str):
    """Tarkistaa, että käyttäjän antama tiedosto on olemassa ja .csv-päätteinen

    Returns:
        True, jos tiedosto löytyy ja sillä on .csv -pääte, muussa tapauksessa False"""
    try:
        with open(file) as file_2:
            file_2.read()
    except:
        return False
    if file[-4:] != ".csv":
        return False
    else:
        return True

def process_file(file:str, name:str):
    """Lähettää tiedoston prosessoitavaksi

    Args:
        file: Tilitiedoston polku + nimi yhdistettynä
        name: Tilille annettu nimi

    Returns:
        Palauttaa TKService()-instanssin
    """
    account = TKService(name)
    account.summary(file)
    ui.queries.choose_offset_account(account)
    repositories.save_data.process_account(account, file)
    return account

def run():
    """Käyttöliittymä, huolehtii toimintavalikosta"""
    console = Console()
    dialog = [" 1 - Lisää Nordean tiliote", " 2 - Lisää S-Pankin tiliote", " 3 - Tulosta raportti", 
              " 4 - Etsi tapahtumia nimellä", " 5 - Yhdistä kaikki tilit", " 6 - Lopeta"]
    available_choices = ["1", "2", "6"]
    saved = len(get_account_names())
    console.print("\n Voit kokeilla ohjelmaa lataushakemiston tiedostoilla Nordea.csv ja S-Pankki.csv")
    if saved > 0:
        available_choices.extend(["3", "4"])
    if saved > 1:
        available_choices.append("5")
    while True: 
        available_choices.sort()
        cowsay.cow(" Valitse toiminto! ")
        for choice in available_choices:
            console.print(dialog[int(choice)-1])
        choice = Prompt.ask(" Valitse toiminto ", choices = available_choices)
        if choice in ["1", "2"]:
            banks = ["", "Nordea", "S-Pankki"]
            file, name = get_file(banks[int(choice)])
            account = process_file(file, name)
            saved += 1
            if "3" not in available_choices:
                available_choices.append("3")
            if "4" not in available_choices:
                available_choices.append("4")
            if saved > 1 and "5" not in available_choices:
                available_choices.append("5")
        elif choice == "3":
            ui.queries.choose_account_for_report()
        elif choice == "4":
            ui.queries.search_events_by_name()
        elif choice == "5":
            accounts = repositories.save_data.get_account_names()
            combined = []
            for account in accounts:
                if account != "Yhdistetty":
                    combined.append(account)
            repositories.save_data.combine_to_json(combined, "Yhdistetty")
            print_success("Kaikkien tilien tapahtumat koottu tilille Yhdistetty.")
        elif choice == "6":
            exit()
