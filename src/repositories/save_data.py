import os
import json

def save_account(account, test = False):
    new_lines = []
    with open(account.path, "rt", encoding = "utf_8") as readfile:
        lines = readfile.readlines()
    for line in lines[1:]:  # skipataan otsikkorivi
        line = line.split(";")
        amount = line[1].replace(",", ".")
        if line[1][0] == "-":
            if account.offset_account_out[line[5]] != "Lainat":
                new_line = account.name + ";" + line[0] + ";" + amount + ";" + line[5] + ";"
                new_line += account.offset_account_out[line[5]] + "\n"
                new_lines.append(new_line)
            else:
                interest = round(float(amount) * account.interests[line[5]] / account.loans[line[5]], 2)
                payment = round(float(amount) - interest, 2)
                new_line = account.name + ";" + line[0] + ";" + str(payment) + ";"
                new_line += line[5] + ";" + "Lainat" + "\n"
                new_lines.append(new_line)
                new_line = account.name + ";" + line[0] + ";" + str(interest) + ";"
                new_line += line[5] + ";" + "Menot" + "\n"
                new_lines.append(new_line)
        else:
            new_line = account.name + ";" + line[0] + ";" + amount + ";" + line[5] + ";"
            new_line += account.offset_account_in[line[5]] + "\n"
            new_lines.append(new_line)
    if not test:
        dirname = os.path.dirname(__file__)
        data_file_path = os.path.join(dirname, "account_data.csv")
        with open(data_file_path, "a", encoding = "utf8") as writefile:
            writefile.writelines(new_lines)
        save_to_json(new_lines, account)
        print("Tiedot on tallennettu.")
    else:
        dirname = os.path.dirname(__file__)
        data_file_path = os.path.join(dirname, "../tests", "test_account_data.csv")
        with open(data_file_path, "w", encoding = "utf8") as writefile:
            writefile.writelines(new_lines, account)
    return True

def save_to_json(data, account):
    events = {}
    for rivi in data:
        osat = rivi.split(";")
        if osat[0] not in events:
            events[osat[0]] = []
        events[osat[0]].append({"Vuosi": osat[1][:4], "Kk": osat[1][5:7], 
            "Summa": osat[2], "Nimi": osat[3], "Luokka": osat[4].replace("\n", ""),
            "Alaluokka": ""})
    json_string = json.dumps(events, indent = 2)
    name = account.name + ".json"
    with open(name, 'w') as file:
        file.write(json_string) #tallentaa repon juureen

def read_from_json(name, criteria, search):
    filename = name + ".json"
    with open(filename, 'r') as file:
        events = json.loads(file.read())
        total = 0
    for event in events[name]:
        if event[criteria] == search:
            print(f"{search}  {event['Summa']}")
            total += float(event['Summa'])
    print(f"Yhteensä {round(total, 2)}")

    