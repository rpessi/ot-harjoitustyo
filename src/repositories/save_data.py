import os
import json
from config import CSV_FILENAME, ACCOUNTS_FILENAME

def save_account(account, file):
    new_lines = []
    name = account.name
    with open(file, "rt", encoding = "utf_8") as readfile:
        lines = readfile.readlines()
    for line in lines[1:]:  # skipataan otsikkorivi
        line = line.split(";")
        date = line[0]
        event = line[5]
        amount = line[1].replace(",", ".")
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
    data_file_path = os.path.join(os.path.dirname(__file__), CSV_FILENAME)
    with open(data_file_path, "a", encoding = "utf8") as writefile:
        writefile.writelines(new_lines)
    save_to_json(new_lines, name)
    print(" Tiedot on tallennettu.")
    save_account_name(name)
    return True

def save_account_name(name):
    dirname = os.path.dirname(__file__)
    data_file_path = os.path.join(dirname, ACCOUNTS_FILENAME)
    with open(data_file_path, "a", encoding = "utf8") as writefile:
        writefile.write(f"{name}\n")

def get_account_names():
    accounts = []
    dirname = os.path.dirname(__file__)
    data_file_path = os.path.join(dirname, ACCOUNTS_FILENAME)
    if not os.path.isfile(data_file_path):
        return accounts
    with open(data_file_path, "r", encoding = "utf8") as file:
        lines = file.readlines()
        for line in lines:
            if line.replace("\n", "") != "TEST": #nolo tilapäinen paikkaus
                accounts.append(line.replace("\n", ""))
    return accounts

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
    name = name + ".json"
    data_file_path = os.path.join(dirname, name)
    with open(data_file_path, 'w', encoding = 'UTF-8') as file:
        file.write(json_string) #tallentaa repon juureen, under construction

def read_from_json(name, key, value):
    dirname = os.path.dirname(__file__)
    filename = name + ".json"
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
        return
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
