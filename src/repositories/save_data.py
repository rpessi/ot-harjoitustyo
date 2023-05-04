import os
import json
from config import CSV_FILENAME, ACCOUNTS_FILENAME, JSON_PATH, CSV_CONVERTED

def process_account(account, file):
    new_lines = []
    name = account.name
    with open(file, "rt", encoding = "utf_8") as readfile:
        lines = readfile.readlines()
    for line in lines[1:]:  # skipataan otsikkorivi
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

def save_to_csv(new_lines, name):
    data_file_path = os.path.join(os.path.dirname(__file__), CSV_FILENAME)
    with open(data_file_path, "a", encoding = "utf8") as writefile:
        writefile.writelines(new_lines)
    print(" Tiedot on tallennettu.")
    return save_to_json(new_lines, name)

def save_to_json(data:list, name):
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
    with open(data_file_path, 'w', encoding = 'UTF-8') as file:
        file.write(json_string)
    return save_account_name(name)

def save_account_name(name):
    dirname = os.path.dirname(__file__)
    data_file_path = os.path.join(dirname, ACCOUNTS_FILENAME)
    with open(data_file_path, "a", encoding = "utf8") as writefile:
        writefile.write(f"{name}\n")
    return True

def get_account_names():
    accounts = []
    dirname = os.path.dirname(__file__)
    data_file_path = os.path.join(dirname, ACCOUNTS_FILENAME)
    if not os.path.isfile(data_file_path):
        return accounts
    with open(data_file_path, "r", encoding = "utf8") as file:
        lines = file.readlines()
        for line in lines:
            accounts.append(line.replace("\n", ""))
    return accounts

def read_from_json(name, key, value):
    dirname = os.path.dirname(__file__)
    filename = JSON_PATH + name + ".json"
    data_file_path = os.path.join(dirname, filename)
    with open(data_file_path, 'r', encoding = 'UTF-8') as file:
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

def combine_to_json(accounts:list, name):
    if accounts == []:
        print("\n Tallennettuja tilejä ei vielä ole.")
        return accounts
    new_lines = []
    dirname = os.path.dirname(__file__)
    data_file_path = os.path.join(dirname, CSV_FILENAME)
    with open(data_file_path, "rt", encoding = "utf_8") as readfile:
        lines = readfile.readlines()
        for line in lines:
            place = line.find(";")
            if line[:place] in accounts:
                new_lines.append(name + line[place:])
    save_to_json(new_lines, name)
    if name not in get_account_names():
        save_account_name(name)
    print("\n Tilien tapahtumat on nyt yhdistetty tilille Yhdistetty.")
    return accounts

def convert_from_s_pankki(file):
    new_lines = ["otsikkorivi \n"]
    with open(file, "rt", encoding = "utf_8") as readfile:
        lines = readfile.readlines()
        p_h = ""
        for line in lines[1:]:  # skipataan otsikkorivi
            #line.replace("\n", "")
            line  = line.split(";")
            date = line[0][-4:]+line[0][2:5]
            amount = line[2].replace(",", ".").replace("+", "")
            print(amount)
            if amount[0] == '-':
                event = line[5]
            else:
                event = line[4]
            new_lines.append(";".join((date, amount, p_h, p_h, p_h, event, p_h)) + "\n")
    data_file_path = os.path.join(os.path.dirname(__file__), CSV_CONVERTED)
    with open(data_file_path, "w", encoding = "utf8") as writefile:
        writefile.writelines(new_lines)
    print(" Muokatut tiedot on tallennettu tiedostoon NC.csv.")
    return "NC.csv"

def create_cash_flow_report(name):
    dirname = os.path.dirname(__file__)
    filename = JSON_PATH + name + ".json"
    data_file_path = os.path.join(dirname, filename)
    report = {'Cash in': {'Yhteensä': 0}, 'Cash out': {'Yhteensä': 0}}
    with open(data_file_path, 'r', encoding = 'UTF-8') as file:
        events = json.loads(file.read())
        for event in events[name]:
            if event['Summa'][0] == "-":
                if event['Nimi'] not in report['Cash out']:
                    report['Cash out'][event['Nimi']] = 0
                report['Cash out'][event['Nimi']] += round(float(event['Summa']), 2)
                report['Cash out']['Yhteensä'] += round(float(event['Summa']), 2)
            else:
                if event['Nimi'] not in report['Cash out']:
                    report['Cash in'][event['Nimi']] = 0
                report['Cash in'][event['Nimi']] += round(float(event['Summa']), 2)
                report['Cash in']['Yhteensä'] += round(float(event['Summa']), 2)
    return report

def create_result_report(name):
    dirname = os.path.dirname(__file__)
    filename = JSON_PATH + name + ".json"
    data_file_path = os.path.join(dirname, filename)
    report = {'Tulot': {'Yhteensä': 0}, 'Menot': {'Yhteensä': 0}}
    with open(data_file_path, 'r', encoding = 'UTF-8') as file:
        events = json.loads(file.read())
        for event in events[name]:
            if event['Luokka'] == 'Tulot':
                if event['Nimi'] not in report['Tulot']:
                    report['Tulot'][event['Nimi']] = 0
                report['Tulot'][event['Nimi']] += round(float(event['Summa']), 2)
                report['Tulot']['Yhteensä'] += round(float(event['Summa']), 2)
            elif event['Luokka'] == 'Menot':
                if event['Nimi'] not in report['Menot']:
                    report['Menot'][event['Nimi']] = 0
                report['Menot'][event['Nimi']] += round(float(event['Summa']), 2)
                report['Menot']['Yhteensä'] += round(float(event['Summa']), 2)
    return report

def count_changes_in_balance(name):
    dirname = os.path.dirname(__file__)
    filename = JSON_PATH + name + ".json"
    data_file_path = os.path.join(dirname, filename)
    report = {'Oma tili': {'Yhteensä': 0}, 'Lainojen lyhennykset': {'Yhteensä': 0}}
    with open(data_file_path, 'r', encoding = 'UTF-8') as file:
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
