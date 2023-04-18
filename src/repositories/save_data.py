def save_account(account):
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
    print(new_lines)
    with open("account_data.csv", "a", encoding = "utf8") as writefile:
        writefile.writelines(new_lines)
