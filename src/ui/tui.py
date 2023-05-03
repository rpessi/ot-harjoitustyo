from services.tk_service import TKService
import cowsay
import ui.queries
import repositories.save_data
from repositories.save_data import get_account_names, convert_from_s_pankki

def get_file():
    while True:
        file = input( " Anna csv-tiedoston nimi ja polku, esim. src/short.csv: ")
        if check_file(file):
            name = input(" Anna tilin nimi: ")
            return tuple((file, name))
        else:
            print(" Tiedostoa ei löydy tai se ei ole csv-tiedosto.")

def check_file(file):
    try:
        with open(file) as file_2:
            file_2.read()
    except:
        return False
    if file[-4:] != ".csv":
        return False
    else:
        return True

def process_file(file, name):
    account = TKService(name)
    account.summary(file)
    ui.queries.choose_offset_account(account)
    repositories.save_data.process_account(account, file)
    return account

def run():
    dialog = [" 1 - Lisää tiedosto", " 2 - Tulosta lisätyn tiedoston kassavirtalaskelma", " 3 - Tulosta lisätyn tiedoston tuloslaskelma",
              " 4 - Etsi tapahtumia nimellä", " 5 - Yhdistä kaikki tilit", " 6 - Lopeta"]
    available_choices = ["1", "6"]
    saved = len(get_account_names())
    if saved > 0:
        available_choices.append("4")
    if saved > 1:
        available_choices.append("5")
    while True: 
        cowsay.cow(" Valitse toiminto! ")
        available_choices.sort()
        for choice in available_choices:
            print(dialog[int(choice)-1])
        choice = input(" Valinta (anna numero, hyväksy enterillä): ")
        if choice in available_choices:
            if choice == "1":
                file, name = get_file()
                account = process_file(file, name)
                if "2" not in available_choices:
                    available_choices.extend(["2", "3"])
                saved += 1
                if "4" not in available_choices:
                    available_choices.append("4")
                if saved > 1 and "5" not in available_choices:
                    available_choices.append("5")
            elif choice == "2":
                account.print_cashflow()
            elif choice == "3":
                account.print_result()
            elif choice == "4":
                ui.queries.search_events_by_name()
            elif choice == "5":
                accounts = repositories.save_data.get_account_names()
                combined = []
                for account in accounts:
                    if account != "Yhdistetty":
                        combined.append(account)
                repositories.save_data.combine_to_json(combined, "Yhdistetty")
            elif choice == "6":
                #convert_from_s_pankki("S-Pankki.csv")
                exit()
