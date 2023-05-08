import colorama as cr
from colorama import init, Fore, Back, Style
from repositories.save_data import create_cash_flow_report, create_result_report, count_changes_in_balance
from rich.console import Console
from rich.table import Table

def print_account_report(name:str, report_type:int):
    if report_type == 1: #tulos
        report = create_result_report(name)
        income, expense = report['Tulot'], report['Menot']
        last_inc = report['Tulot']['Tulot yhteensä']
        last_exp = report['Menot']['Menot yhteensä']
    if report_type == 2: #kassavirta
        report = create_cash_flow_report(name)
        income, expense = report['Cash in'], report['Cash out']
    if report_type == 3: #tase
        report = count_changes_in_balance(name)
        income, expense = report['Oma tili'], report['Lainojen lyhennykset']
    inc_lines, exp_lines = [], []
    for key, value in income.items():
        inc_lines.append((round(value, 2), key))
    for key, value in expense.items():
        exp_lines.append((round(-value, 2), key))
    inc_lines.sort()
    last = inc_lines.pop()
    inc_lines.reverse()
    inc_lines.append(last)
    exp_lines.sort()
    last = exp_lines.pop()
    exp_lines.reverse()
    exp_lines.append(last)
    if report_type in [1, 2]:
        print_cash_or_result(name, inc_lines, exp_lines, report_type)
    if report_type == 3:
        print_balance(name, inc_lines, exp_lines)

def print_balance(name: str, inc_lines: list, exp_lines: list):
    table = Table(title=f"Muutokset tase-erissä tilillä {name}", title_style = 'bold dark_violet')
    table.add_section()
    table.add_column("Varat/Velat", justify="left", style="bold dark_violet", no_wrap=True)
    table.add_column("Tapahtumat", style="deep_sky_blue4")
    table.add_column("Muutos", justify="right", style="deep_sky_blue4")
    table.add_row("Varat", f"{inc_lines[0][1]}", f"{inc_lines[0][0]}")
    for line in inc_lines[1:len(inc_lines)-1]:
        table.add_row("", f"{line[1]}", f"{line[0]}")
    table.add_row(f"{inc_lines[-1][1]}", "", f"{inc_lines[-1][0]}", end_section=True)
    table.add_row("Velat", f"{exp_lines[0][1]}", f"{exp_lines[0][0]}")
    for line in exp_lines[1:len(exp_lines)-1]:
        table.add_row("", f"{line[1]}", f"{line[0]}")
    table.add_row(f"{exp_lines[-1][1]}", "", f"{exp_lines[-1][0]}")
    console = Console()
    print("\n")
    console.print(table)
    print_success("Tase-erien muutosten tulostus")

def print_cash_or_result(name:str, inc_lines:list, exp_lines:list, report_type:int):
    titles = ["", "Tuloslaskelma", "Kassavirtalaskelma"]
    table = Table(title=f"{titles[report_type]} tililtä {name}", title_style = 'bold dark_violet')
    table.add_column("Tulot/Menot", justify="left", style="bold dark_violet", no_wrap=True)
    table.add_column("Tapahtumat", style="deep_sky_blue4")
    table.add_column("Summa", justify="right", style="deep_sky_blue4")
    table.add_row("Tulot", f"{inc_lines[0][1]}", f"{inc_lines[0][0]}")
    for line in inc_lines[1:len(inc_lines)-1]:
        table.add_row("", f"{line[1]}", f"{line[0]}")
    table.add_row(f"{inc_lines[-1][1]}", "", f"{inc_lines[-1][0]}")
    table.add_section()
    table.add_row("Menot", f"{exp_lines[0][1]}", f"{exp_lines[0][0]}")
    for line in exp_lines[1:len(exp_lines)-1]:
        table.add_row("", f"{line[1]}", f"{line[0]}")
    table.add_row(f"{exp_lines[-1][1]}", "", f"{exp_lines[-1][0]}")
    console = Console()
    print("\n")
    console.print(table)
    if report_type == 1:
        print_success("Tuloslaskelman tulostus")
    if report_type == 2:
        print_success("Kassavirtalaskelman tulostus")

def print_success(message:str):
    print("\n")
    console = Console()
    grid = Table.grid(expand=True)
    grid.add_column(max_width=35)
    grid.add_column(justify="left")
    grid.add_column(width=20)
    grid.add_row(f"[deep_sky_blue4] {message}", "[bold magenta]VALMIS[green4]:heavy_check_mark:", "")
    console.print(grid)
    print("\n")