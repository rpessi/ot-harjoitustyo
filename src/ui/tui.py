from services.tk_service import TKService
import cowsay
import ui.queries
import repositories.save_data

def get_file():
    while True:
        file = input(
            "Anna csv-tiedoston nimi ja polku, esim. src/short.csv: ")
        if check_file(file):
            name = input("Anna tilin nimi: ")
            return tuple((file, name))
        else:
            print("Tiedostoa ei löydy tai se ei ole csv-tiedosto.")

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
    account = TKService(name, file)
    account.summary(account.path)
    ui.queries.choose_offset_account(account)
    repositories.save_data.save_account(account)
    return account

def run():
    file_received = False
    while True: 
        cowsay.cow(" Valitse toiminto! ")
        print(f" 1 - Lisää tiedosto")
        print(f" 2 - Tulosta lisätyn tiedoston kassavirtalaskelma")
        print(f" 3 - Tulosta lisätyn tiedoston tuloslaskelma")
        print(f" 4 - Lopeta")
        choice = input(" Valinta (anna numero, hyväksy enterillä): ")
        if choice in ["1", "2", "3", "4"]:
            if choice == "1":
                file, name = get_file()
                account = process_file(file, name)
                file_received = True
            elif choice == "2":
                if not file_received:
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
                exit()
