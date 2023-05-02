import os
import json

def save_account(account, file, test = False):
    new_lines = []
    with open(file, "rt", encoding = "utf_8") as readfile:
        lines = readfile.readlines()
    for line in lines[1:]:  # skipataan otsikkorivi
        line = line.split(";")
        amount = line[1].replace(",", ".")
        if line[1][0] == "-":
            if account.offset_account_out[line[5]] != "Lainat":
                new_lines.append(account.name + ";" + line[0] + ";" + amount + ";" + line[5] + ";" \
                    + account.offset_account_out[line[5]] + "\n")
            else:
                interest = round(float(amount) * account.interests[line[5]] \
                                 / account.loans[line[5]], 2)
                payment = round(float(amount) - interest, 2)
                new_lines.append(account.name + ";" + line[0] + ";" + str(payment) + ";" \
                        + line[5] + ";" + "Lainat" + "\n")
                new_lines.append(account.name + ";" + line[0] + ";" + str(interest) + ";" \
                    + line[5] + ";" + "Menot" + "\n")
        else:
            new_lines.append(account.name + ";" + line[0] + ";" + amount + ";" + line[5] + ";" \
                + account.offset_account_in[line[5]] + "\n")
    dirname = os.path.dirname(__file__)
    if not test:
        data_file_path = os.path.join(dirname, "account_data.csv")
        with open(data_file_path, "a", encoding = "utf8") as writefile:
            writefile.writelines(new_lines)
        save_to_json(new_lines, account)
        print(" Tiedot on tallennettu.")
    else:
        data_file_path = os.path.join(dirname, "../tests", "test_account_data.csv")
        with open(data_file_path, "w", encoding = "utf8") as writefile:
            writefile.writelines(new_lines)
    save_account_name(account)
    return True

def save_account_name(account):
    dirname = os.path.dirname(__file__)
    data_file_path = os.path.join(dirname, "account_names.csv")
    with open(data_file_path, "a", encoding = "utf8") as writefile:
        writefile.write(f"{account.name}\n")

def get_account_names():
    accounts = []
    dirname = os.path.dirname(__file__)
    data_file_path = os.path.join(dirname, "account_names.csv")
    with open(data_file_path, "r", encoding = "utf8") as file:
        lines = file.readlines()
        for line in lines:
            if line.replace("\n", "") != "TEST": #nolo tilapäinen paikkaus
                accounts.append(line.replace("\n", ""))
    return accounts

def save_to_json(data, account):
    events = {}
    for rivi in data:
        osat = rivi.split(";")
        if osat[0] not in events:
            events[osat[0]] = []
        events[osat[0]].append({"Vuosi": osat[1][:4], "Kk": osat[1][5:7],
            "Summa": osat[2], "Nimi": osat[3], "Luokka": osat[4].replace("\n", ""),
            "Alaluokka": ""})
    json_string = json.dumps(events, indent = 2, ensure_ascii = False)
    name = account.name + ".json"
    with open(name, 'w', encoding = 'UTF-8') as file:
        file.write(json_string) #tallentaa repon juureen, under construction

def read_from_json(name, key, value):
    filename = name + ".json"
    with open(filename, 'r', encoding = 'UTF-8') as file:
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
