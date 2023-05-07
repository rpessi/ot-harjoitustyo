import colorama as cr
from colorama import init, Fore, Back, Style
from repositories.save_data import create_cash_flow_report, create_result_report, count_changes_in_balance
from rich.console import Console
from rich import inspect
from rich.table import Table

def print_cash_report(name):
    report = create_cash_flow_report(name)
    cash_in, cash_out = report['Cash in'], report['Cash out']
    cash_in_items, cash_out_items = [], []
    for key, value in cash_in.items():
        cash_in_items.append((value, key))
    for key, value in cash_out.items():
        cash_out_items.append((value, key))
    printlines = [f"   Kassavirtalaskelma tililtä {name} \n\n   Tulot \n"]
    cash_in_items.sort()
    last = cash_in_items.pop()
    cash_in_items.reverse()
    cash_in_items.append(last)
    in_lines = cash_in_items.copy()
    for item in cash_in_items:
        printlines.append(f"     {item[1]:<30} {item[0]:12.2f}")
    printlines.append(f"\n   Menot \n")
    cash_out_items.sort()
    cash_out_items.reverse()
    last = cash_out_items.pop()
    cash_out_items.reverse()
    cash_out_items.append(last)
    out_lines = cash_out_items.copy()
    for item in cash_out_items:
        printlines.append(f"     {item[1]:<30} {-item[0]:12.2f}")
    console_printing(printlines)
    #table_printing(name) #käytetty koeprinttauksiin keskeneräisellä funktiolla

def printing(lines): #poistuva, mutta ei deletoida vielä
    init()
    print(cr.ansi.clear_screen())
    border = "\n($.$) ($.$) ($.$) ($.$) ($.$) ($.$) ($.$) ($.$) ($.$)\n"
    print(Fore.GREEN + border + Style.DIM + Style.RESET_ALL)
    for line in lines:
        print(Fore.MAGENTA + line + Style.BRIGHT + Style.RESET_ALL)
    print(Fore.GREEN + border + Style.DIM + Style.RESET_ALL)

def console_printing(lines):
    console = Console()
    border = "\n($.$) ($.$) ($.$) ($.$) ($.$) ($.$) ($.$) ($.$) ($.$)\n"
    console.print(border, style = 'bold green')
    for line in lines:
        console.print(line, style = 'magenta')
    console.print(border, style = 'bold green')

def table_printing(name): #testailuasennossa kovakoodattuna, huom. exit() lopussa
    table = Table(title=f"Kassavirtalaskelma tililtä {name}", title_style = 'bold blue')
    table.add_section
    table.add_column("Tulot/Menot", justify="left", style="cyan", no_wrap=True)
    table.add_column("Tapahtumat", style="magenta")
    table.add_column("Summa", justify="right", style="green")
    #table.add_row("Tulot", "", "")
    table.add_row("Tulot", "PALKKA", "19679.96")
    table.add_row("", "OPINTOTUKI", "700.00")
    table.add_row("Yhteensä", "", "20379.96", end_section=True)
    #table.add_row("Menot", "", "")
    table.add_row("Menot", "NORDEA LAINAT", "4607.71")
    table.add_row("", "NORDEA RAHOITUS SUOMI OY ", "3690.93")
    table.add_row("", "Asunto Oy Helsingin Välimeri", "2995.65")
    table.add_row("", "Elisa Oyj", "272.59")
    table.add_row("Yhteensä", "", "11566.88")
    console = Console()
    console.print(table)
    print("\n\n")
    grid = Table.grid(expand=True)
    grid.add_column(max_width=35)
    grid.add_column(justify="left")
    grid.add_column(width=20)
    grid.add_row("[green] Kassavirtalaskelma tulostettu", "[bold magenta]VALMIS[green]:heavy_check_mark:", "")
    console.print(grid)
    print("\n\n")
    exit()
