from services.tk_service import TKService
import cowsay
import ui.queries

# simppeli tekstikäyttöliittymä testailua varten
def get_file():
    while True:
        file = input(
            "Anna csv-tiedoston nimi ja polku, esim. Home/documents/tiliote.csv: ")
        if check_file(file):
            name = input("Anna tilin nimi: ")
            return tuple((file, name))
        else:
            print("Tiedostoa ei löydy tai se ei ole csv-tiedosto.")

def check_file(file):  # onko tän paikka täällä, oisko joku muu paikka parempi?
    # print("päästiin check_file -funktioon")
    # print(file)
    try:
        with open(file) as file_2:
            file_2.read()  # tehdään jotain, että filu menee kiinni, kai?
    except:
        return False
    if file[-4:] != ".csv":
        #print("if-lausekkeessa", file[-4:])
        return False
    else:
        # print("on .csv", file[-4:])
        return True

def process_file(file, name):  # ottaa tuplen (file, name) ja lähettää service-kerrokseen
    print("tultiin tiedoston prosessointiin")
    account = TKService(name, file)
    account.summary(account.path)
    ui.queries.choose_offset_account(account)
    return account

def settings():
    #summary-funktion raja, jota pienemmät tapahtumat niputetaan yhteen
    #tilin alkusaldo
    pass

def run():
    while True: 
        cowsay.cow("Valitse toiminto!")
        print(f"1 - Lisää tiedosto") #ohjaa tapahtumien luokitteluun
        print(f"2 - Tulosta yhteenveto")
        print(f"3 - Lopeta")
        choice = input("Valinta (anna numero, hyväksy enterillä): ")
        if choice in ["1", "2", "3"]:
            if choice == "1":
                file, name = get_file()
                account = process_file(file, name)
            elif choice == "2":
                account.print_summary()
            elif choice == "3":
                exit()
