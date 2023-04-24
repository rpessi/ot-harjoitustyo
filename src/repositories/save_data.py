import os

def save_account(account, test = None):
    new_lines = []
    with open(account.path, "rt", encoding = "utf_8") as readfile:
        lines = readfile.readlines()
    for line in lines[1:]:  # skipataan otsikkorivi
        line = line.split(";")
        new_line = account.name + ";" + line[0] + ";" + line[1] + ";" + line[5] + ";"
        if line[1][0] == "-":
            new_line += account.offset_account_out[line[5]] + "\n"
        else:
            new_line += account.offset_account_in[line[5]] + "\n"
        new_lines.append(new_line)
    dirname = os.path.dirname(__file__)
    if test == None:
        data_file_path = os.path.join(dirname, "account_data.csv")
        with open(data_file_path, "a", encoding = "utf8") as writefile:
            writefile.writelines(new_lines)
        print("Tiedot on tallennettu.")
    else:
        print (account.offset_account_out)
        data_file_path = os.path.join(dirname, "tests", "test_account_data.csv")
        with open(data_file_path, "w", encoding = "utf8") as writefile:
            writefile.writelines(new_lines) #ei toimi ilman offset_account-sanakirjoja