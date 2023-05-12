"""Tiedon pysyväistallennuksesta ja siihen liittyvistä funktioista vastaava osio"""
import os
import json
from config import CSV_FILENAME, ACCOUNTS_FILENAME, JSON_PATH, CSV_CONVERTED

def process_account(account, file:str):
    """Toiminto käyttäjän antaman tiedoston käsittelyyn ja muokkaamiseen tallennusta varten

        Args:
            account: TKService()-instanssi
            file: käsiteltävän tiedoston polku ja nimi

        Returns:
            Palauttaa komentoketjun kautta True, kun tiedot on talletettu csv- ja json-muotoisina
            ja kun tilin nimi on talletettu tilien nimiä tallentavaan csv-tiedoston"""
    new_lines = []
    name = account.name
    with open(file, "rt", encoding = "utf-8") as readfile:
        lines = readfile.readlines()
    for line in lines[1:]:
        line  = line.split(";")
        date, event, amount = line[0], line[5],line[1].replace(",", ".")
        if line[1][0] == "-":
            offset = account.offset_account_out[event]
            if offset != "Lainat":
                new_lines.append(";".join((name, date, amount, event, offset)) + "\n")
            else:
                interest = round(float(amount) * account.interests[event] / account.loans[event], 2)
                payment = round(float(amount) - interest, 2)
                new_lines.append(";".join((name, date, str(payment), event, "Lainat")) + "\n")
                new_lines.append(";".join((name, date, str(interest), event, "Menot")) + "\n")
        else:
            offset = account.offset_account_in[event]
            new_lines.append(";".join((name, date, amount, event, offset)) + "\n")
    return save_to_csv(new_lines, name)

def save_to_csv(new_lines:list, name:str):
    """Toiminto, joka tallentaa process_account() -funktion prosessoimat tiedot csv-tiedostoon

        Args:
            new_lines: Prosessoidut tiedot, jotka halutaan tallentaa
            name: Käyttäjän tilille antama nimi, joka välitetään eteenpäin seuraavalle funktiolle

        Returns:
            palauttaa komentoketjun kautta True, kun tallennusfunktiot on käyty läpi"""

    data_file_path = os.path.join(os.path.dirname(__file__), CSV_FILENAME)
    with open(data_file_path, "a", encoding = "utf-8") as writefile:
        writefile.writelines(new_lines)
    return save_to_json(new_lines, name)

def save_to_json(data:list, name):
    """Tilitietojen json-muotoisesta tallennuksesta vastaava toiminto

    Args:
        data: Lista tallennettavista riveistä
        name: Käyttäjän tilille antama nimi

    Returns:
        Palauttaa komentoketjun kautta True, kun tallennusfunktiot on käyty läpi
        """
    events = {}
    for rivi in data:
        osat = rivi.split(";")
        if osat[0] not in events:
            events[osat[0]] = []
        events[osat[0]].append({"Vuosi": osat[1][:4], "Kk": osat[1][5:7],
            "Summa": osat[2], "Nimi": osat[3], "Luokka": osat[4].replace("\n", ""),
            "Alaluokka": ""})
    json_string = json.dumps(events, indent = 2, ensure_ascii = False)
    dirname = os.path.dirname(__file__)
    filename = JSON_PATH + name + ".json"
    data_file_path = os.path.join(dirname, filename)
    with open(data_file_path, 'w', encoding = 'utf-8') as file:
        file.write(json_string)
    if name != 'Yhdistetty':
        return save_account_name(name)
    return True

def save_account_name(name:str):
    """Toiminto, joka tallentaa käyttäjän antaman tilin nimen

        Args:
            name: Tilin nimi, joka tallennetaan pysyvästi

        Returns:
            True
    """
    dirname = os.path.dirname(__file__)
    data_file_path = os.path.join(dirname, ACCOUNTS_FILENAME)
    with open(data_file_path, "a", encoding = "utf-8") as writefile:
        writefile.write(f"{name}\n")
    return True

def get_account_names():
    """Toiminto, joka lukee tiedostosta sinne tallennettujen tilien nimet

        Returns:
            Palauttaa tallennettujen tilien nimet listana tai tyhjän listan, jos tallennettuja
            tietoja ei ole
    """
    accounts = []
    dirname = os.path.dirname(__file__)
    data_file_path = os.path.join(dirname, ACCOUNTS_FILENAME)
    if not os.path.isfile(data_file_path):
        return accounts
    with open(data_file_path, "r", encoding = "utf-8") as file:
        lines = file.readlines()
        for line in lines:
            accounts.append(line.replace("\n", ""))
    return accounts

def read_from_json(name:str, key:str, value:str):
    """Toiminto json-tallennettujen tietojen lukemiseen ja hakujen tekemiseen

        Args: 
            name: Tilin nimi, jolta tapahtumia haetaan
            key: Hakuavain, esimerkiksi 'Nimi' tai 'Vuosi'; sanakirjan avain, jolla haetaan
            value: Hakuehto, jolla haetaan

        Returns:
            Palauttaa löydettyjen tapahtumien yhteissumman
        """""
    dirname = os.path.dirname(__file__)
    filename = JSON_PATH + name + ".json"
    data_file_path = os.path.join(dirname, filename)
    with open(data_file_path, 'r', encoding = 'utf-8') as file:
        events = json.loads(file.read())
        total = 0
    for event in events[name]:
        if event[key].casefold().startswith(value.casefold()):
            print(f" {event['Kk']}/{event['Vuosi']} {event[key]}  {event['Summa']}")
            total += float(event['Summa'])
    if total != 0:
        print(f" Yhteensä {round(total, 2)}")
    else:
        print(f" Tililtä {name} ei löydy tapahtumia haulla '{value}'.")
    return round(total, 2)

def combine_to_json(accounts:list, name:str):
    """Toiminto, jolla yhdistetään useamman tilin tiedot samaan tiedostoon. 

        Args:
            accounts = lista tilien nimistä
            name: nimi, jolla yhdistettävät tilit tallennetaan

        Returns:
            accounts: Palauttaa parametrina annetun listan, jos tallennus onnistui. Tyhjä lista
            palautetaan, jos tallennettavia tilejä ei ole
            """
    if not get_account_names():
        return accounts
    new_lines = []
    dirname = os.path.dirname(__file__)
    data_file_path = os.path.join(dirname, CSV_FILENAME)
    with open(data_file_path, "rt", encoding = "utf-8") as readfile:
        lines = readfile.readlines()
        for line in lines:
            place = line.find(";")
            if line[:place] in accounts and line[:place] != "Yhdistetty":
                new_lines.append(name + line[place:])
    save_to_json(new_lines, name)
    current_accounts = get_account_names()
    if name not in current_accounts:
        save_account_name(name)
    return accounts

def convert_from_s_pankki(file:str):
    """Toiminto, joka muokkaa S-Pankin tiliotteen ohjelmalle sopivaan muotoon ja
        tallentaa sen reposition juureen

        Args:
            file: Tiedoston polku ja nimi, jonka käyttäjä antaa muokattavaksi

        Returns:
            "NC.csv": Palauttaa nimen, jolla tiedosto on tallennettu
    """
    new_lines = ["otsikkorivi \n"]
    with open(file, "rt", encoding = "utf_8") as readfile:
        lines = readfile.readlines()
        p_h = ""
        for line in lines[1:]:  # skipataan otsikkorivi
            #line.replace("\n", "")
            line  = line.split(";")
            date = line[0][-4:]+line[0][2:5]
            amount = line[2].replace(",", ".").replace("+", "")
            if amount[0] == '-':
                event = line[5]
            else:
                event = line[4]
            new_lines.append(";".join((date, amount, p_h, p_h, p_h, event, p_h)) + "\n")
    data_file_path = os.path.join(os.path.dirname(__file__), CSV_CONVERTED)
    with open(data_file_path, "w", encoding = "utf-8") as writefile:
        writefile.writelines(new_lines)
    return "NC.csv"

def create_cash_flow_report(name:str):
    """Toiminto, joka luo kassavirtaraportin tilitietojen JSON-tallennetusta muodosta

        Args:
            name: Tilin nimi

        Returns:
            report: Sanakirja, johon on koottu kassavirtalaskelman tiedot
    """
    dirname = os.path.dirname(__file__)
    filename = JSON_PATH + name + ".json"
    data_file_path = os.path.join(dirname, filename)
    report = {'Cash in': {}, 'Cash out': {}}
    with open(data_file_path, 'r', encoding = 'utf-8') as file:
        events = json.loads(file.read())
        total_cash_in, total_cash_out = 0, 0
        for event in events[name]:
            if event['Summa'][0] != "-":
                if event['Nimi'] not in report['Cash in']:
                    report['Cash in'][event['Nimi']] = 0
                report['Cash in'][event['Nimi']] += round(float(event['Summa']), 2)
                total_cash_in += round(float(event['Summa']), 2)
        report['Cash in']['Tulot yhteensä'] = total_cash_in
        for event in events[name]:
            if event['Summa'][0] == "-":
                if event['Nimi'] not in report['Cash out']:
                    report['Cash out'][event['Nimi']] = 0
                report['Cash out'][event['Nimi']] += round(float(event['Summa']), 2)
                total_cash_out += round(float(event['Summa']), 2)
        report['Cash out']['Menot yhteensä'] = total_cash_out
    return report

def create_result_report(name:str):
    """Toiminto, joka luo tuloslaskelman tilitietojen JSON-tallennetusta muodosta

        Args:
            name: Tilin nimi

        Returns:
            report: Sanakirja, johon on koottu tuloslaskelman tiedot
    """
    dirname = os.path.dirname(__file__)
    filename = JSON_PATH + name + ".json"
    data_file_path = os.path.join(dirname, filename)
    report = {'Tulot': {}, 'Menot': {}}
    with open(data_file_path, 'r', encoding = 'utf-8') as file:
        events = json.loads(file.read())
        total_income, total_expense = 0, 0
        for event in events[name]:
            if event['Luokka'] == 'Tulot':
                if event['Nimi'] not in report['Tulot']:
                    report['Tulot'][event['Nimi']] = 0
                report['Tulot'][event['Nimi']] += round(float(event['Summa']), 2)
                total_income += round(float(event['Summa']), 2)
        report['Tulot']['Tulot yhteensä'] = round(total_income, 2)
        for event in events[name]:
            if event['Luokka'] == 'Menot':
                if event['Nimi'] not in report['Menot']:
                    report['Menot'][event['Nimi']] = 0
                report['Menot'][event['Nimi']] += round(float(event['Summa']), 2)
                total_expense += round(float(event['Summa']), 2)
        report['Menot']['Menot yhteensä'] = round(total_expense, 2)
    return report

def count_changes_in_balance(name:str):
    """Toiminto, joka laskee tase-erien muutokset tilitietojen JSON-tallennetusta muodosta

        Args:
            name: Tilin nimi

        Returns:
            report: Sanakirja, johon on koottu tiedot tase-erien muutoksista
    """
    dirname = os.path.dirname(__file__)
    filename = JSON_PATH + name + ".json"
    data_file_path = os.path.join(dirname, filename)
    report = {'Oma tili': {'Yhteensä': 0}, 'Lainojen lyhennykset': {'Yhteensä': 0}}
    with open(data_file_path, 'r', encoding = 'utf-8') as file:
        events = json.loads(file.read())
        for event in events[name]:
            if event['Luokka'] == 'Lainat':
                if event['Nimi'] not in report['Lainojen lyhennykset']:
                    report['Lainojen lyhennykset'][event['Nimi']] = 0
                report['Lainojen lyhennykset'][event['Nimi']] += -round(float(event['Summa']), 2)
                report['Lainojen lyhennykset']['Yhteensä'] += -round(float(event['Summa']), 2)
            elif event['Luokka'] == 'Oma tili':
                if event['Nimi'] not in report['Oma tili']:
                    report['Oma tili'][event['Nimi']] = 0
                report['Oma tili'][event['Nimi']] += -round(float(event['Summa']), 2)
                report['Oma tili']['Yhteensä'] += -round(float(event['Summa']), 2)
    return report
