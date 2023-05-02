from services.tk_service import TKService
import cowsay
import ui.queries
import repositories.save_data

def get_file():
    while True:
        file = input( "Anna csv-tiedoston nimi ja polku, esim. src/short.csv: ")
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
    repositories.save_data.save_account(account, file)
    return account

def run():
    # periaatteessa voisi laittaa tähän vaikka account = None,
    # ja sitten tarkistaa accountin arvo apumuuttujan käyttämisen sijaan.
    # ylimääräisen muuttujan käyttäminen ei tuo tässä lisäarvoa
    file_received = False
    while True:
        cowsay.cow(" Valitse toiminto! ")
        # näistä voi poistaa f:t
        print(f" 1 - Lisää tiedosto")
        print(f" 2 - Tulosta lisätyn tiedoston kassavirtalaskelma")
        print(f" 3 - Tulosta lisätyn tiedoston tuloslaskelma")
        print(f" 4 - Etsi tapahtumia nimellä")
        print(f" 5 - Lopeta")
        choice = input(" Valinta (anna numero, hyväksy enterillä): ")
        if choice in ["1", "2", "3", "4", "5"]:
            if choice == "1":
                file, name = get_file()
                account = process_file(file, name)
                file_received = True
            # Tässä on kaksi kertaa `if not file_received`, choice 2 ja 3 voisi vaikka yhdistää
            # samaan iffiin jonka sisällä katsotaan onko tiedostoa annettu, ja sitten
            # katsotaan onko 2 vai 3
            elif choice == "2":
                if not file_received:
                    # tyhjän printin voisi korvata laittamalla seuraavan eteen \n
                    print()
                    print(" o_O Lisää ensin tiedosto! o_O")
                else:
                    account.print_cashflow()
            elif choice == "3":
                if not file_received:
                    print()
                    print(" o_O Lisää ensin tiedosto! o_O")
                else:
                    account.print_result()
            elif choice == "4":
                ui.queries.search_events_by_name()
            elif choice == "5":
                exit()
