import os

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
                interest = float(amount) * account.splits[line[5]] / account.loans[line[5]]
                payment = float(amount) - interest
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
        print("Tiedot on tallennettu.")
    else:
        dirname = os.path.dirname(__file__)
        data_file_path = os.path.join(dirname, "../tests", "test_account_data.csv")
        with open(data_file_path, "w", encoding = "utf8") as writefile:
            writefile.writelines(new_lines)
