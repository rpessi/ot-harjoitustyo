import colorama as cr
from colorama import init, Fore, Back, Style
from repositories.save_data import create_cash_flow_report, create_result_report, count_changes_in_balance

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
    for item in cash_in_items:
        printlines.append(f"     {item[1]:<30} {item[0]:12.2f}")
    printlines.append(f"\n   Menot \n")
    cash_out_items.sort()
    cash_out_items.reverse()
    for item in cash_out_items:
        printlines.append(f"     {item[1]:<30} {-item[0]:12.2f}")
    printing(printlines)

def printing(lines):
    init()
    print(cr.ansi.clear_screen())
    border = "\n($.$) ($.$) ($.$) ($.$) ($.$) ($.$) ($.$) ($.$) ($.$)\n"
    print(Fore.GREEN + border + Style.DIM + Style.RESET_ALL)
    for line in lines:
        print(Fore.MAGENTA + line + Style.BRIGHT + Style.RESET_ALL)
    print(Fore.GREEN + border + Style.DIM + Style.RESET_ALL)
