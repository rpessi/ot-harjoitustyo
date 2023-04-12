from ..services.tk_service import TKService

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
    account = TKService(file, name)


if __name__ == "__main__":
    file_path = "/home/rpessi/ohte/src/tests/Nordea_test_file.csv"
    # print(check_file(file_path))
    file, name = get_file()
    print(file, name)
    process_file(file, name)
