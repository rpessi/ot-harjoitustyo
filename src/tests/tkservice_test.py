import unittest
from services.tk_service import TKService
from repositories.save_data import process_account, get_account_names, read_from_json, combine_to_json
from repositories.save_data import combine_to_json, convert_from_s_pankki, create_cash_flow_report
from repositories.save_data import create_result_report, count_changes_in_balance
import os
from config import CSV_FILENAME, ACCOUNTS_FILENAME

class TestTKService(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.data = os.path.join(dirname, "Nordea.csv")
        if os.path.exists(os.path.join(dirname, ACCOUNTS_FILENAME)):
            os.remove(os.path.join(dirname, ACCOUNTS_FILENAME))
        if os.path.exists(os.path.join(dirname, CSV_FILENAME)):
            os.remove(os.path.join(dirname, CSV_FILENAME))
        if os.path.exists(os.path.join(dirname, "../tests/TEST.json")):
            os.remove(os.path.join(dirname, "../tests/TEST.json"))
        if os.path.exists(os.path.join(dirname, "../tests/TEST2.json")):
            os.remove(os.path.join(dirname, "../tests/TEST2.json"))
        if os.path.exists(os.path.join(dirname, "../tests/UNITED.json")):
            os.remove(os.path.join(dirname, "../tests/UNITED.json"))
        self.account = TKService("TEST")
        self.account.interests["NORDEA LAINAT 1"] = -500.0
        self.account.interests["NORDEA LAINAT 2"] = -1500.0
        self.account.loans["NORDEA LAINAT 1"] = -8485.83
        self.account.loans["NORDEA LAINAT 2"] = -13211.29
        self.account.offset_account_in['PALKKA'] = 'Tulot'
        self.account.offset_account_in['PIRJO PYTHON'] = 'Lainat'
        self.account.offset_account_in['MJUK GROUP AB'] = 'Oma tili'
        self.account.offset_account_out['NORDEA LAINAT 1'] = 'Lainat'
        self.account.offset_account_out['NORDEA LAINAT 2'] = 'Lainat'
        self.account.offset_account_out['Asunto Oy Helsingin Välimeri'] = 'Menot'
        self.account.offset_account_out['NORDEA RAHOITUS SUOMI OY'] = 'Menot'
        self.account.offset_account_out['IF VAKUUTUS'] = 'Menot'
        self.account.offset_account_out['Elisa Oyj'] = 'Menot'
        self.account2 = TKService("TEST2")
        self.data2 = os.path.join(dirname, "Nordea2.csv")
        self.account2.offset_account_in['PALKKA'] = 'Tulot'
        self.account2.offset_account_out['Elisa Oyj'] = 'Menot'


    def test_summary_counts_money_out_correctly(self):
        self.account.summary(self.data)
        key1 = "NORDEA RAHOITUS SUOMI OY"
        key2 = "IF VAKUUTUS"
        self.assertEqual(round(self.account.money_out[key1], 2), -8129.21)
        self.assertEqual(round(self.account.money_out[key2], 2), -1909.96)

    def test_summary_counts_money_in_correctly(self):
        self.account.summary(self.data)
        key1 = "PIRJO PYTHON"
        key2 = "PALKKA"
        self.assertEqual(round(self.account.money_in[key1], 2), 3150.00)
        self.assertEqual(round(self.account.money_in[key2], 2), 37383.03)

    def test_process_account_works(self):
        result = process_account(self.account, self.data)
        self.assertEqual(result, True)

    def test_get_account_names_works(self):
        process_account(self.account, self.data)
        result = get_account_names()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "TEST")

    def test_read_from_json_works(self):
        process_account(self.account, self.data)
        result = read_from_json(self.account.name, 'Nimi', 'elisa')
        self.assertEqual(result, -539.74)
        result = read_from_json(self.account.name, 'Nimi', 'asun')
        self.assertEqual(result, -5796.3) 

    def test_combine_to_json_works(self):
        result0 = combine_to_json([], "UNITED")
        self.assertEqual(result0, [])
        process_account(self.account, self.data)
        process_account(self.account2, self.data2)
        combine_to_json(["TEST", "TEST2"], "UNITED")
        result1 = get_account_names()
        self.assertEqual(result1, ['TEST', 'TEST2', 'UNITED'])
        result2, result3 = read_from_json('UNITED', 'Nimi', 'eli'), read_from_json('UNITED', 'Nimi', 'alt')
        self.assertEqual(result2, -999.63)
        self.assertEqual(result3, 0)

    def test_convert_from_spankki_works_correctly(self):
        dirname = os.path.dirname(__file__)
        data = os.path.join(dirname, "S-Pankki.csv")
        newdata = convert_from_s_pankki(data)
        datapath = os.path.join(dirname, newdata)
        result = os.path.isfile(datapath)
        self.assertEqual(result, True)

    def test_create_cash_flow_report_works_correctly_with_one_account(self):
        process_account(self.account, self.data)
        report = create_cash_flow_report(self.account.name)
        tot_income = report['Cash in']['Tulot yhteensä']
        tot_exp = report['Cash out']['Menot yhteensä']
        self.assertEqual(round(tot_income, 2), 40808.04)
        self.assertEqual(round(tot_exp, 2), -38072.33)

    def test_create_cash_flow_report_works_correctly_with_two_accounts(self):
        process_account(self.account, self.data)
        process_account(self.account2, self.data2)
        combine_to_json(["TEST", "TEST2"], "UNITED")
        report = create_cash_flow_report("UNITED")
        tot_income = report['Cash in']['Tulot yhteensä']
        tot_exp = report['Cash out']['Menot yhteensä']
        self.assertEqual(round(tot_income, 2), 71410.03)
        self.assertEqual(round(tot_exp, 2), -38532.22)

    def test_create_result_report_works_correctly_with_one_account(self):
        process_account(self.account, self.data)
        report = create_result_report(self.account.name)
        tot_income = report['Tulot']['Tulot yhteensä']
        tot_exp = report['Menot']['Menot yhteensä']
        self.assertEqual(round(tot_income, 2), 37383.03)
        self.assertEqual(round(tot_exp, 2), -18375.19)

    def test_create_result_report_works_correctly_with_two_accounts(self):
        process_account(self.account, self.data)
        process_account(self.account2, self.data2)
        combine_to_json(["TEST", "TEST2"], "UNITED")
        report = create_result_report("UNITED")
        tot_income = report['Tulot']['Tulot yhteensä']
        tot_exp = report['Menot']['Menot yhteensä']
        self.assertEqual(round(tot_income, 2), 67985.02)
        self.assertEqual(round(tot_exp, 2), -18835.08)

    def test_count_changes_in_balance_works_with_one_account(self):
        process_account(self.account, self.data)
        report = count_changes_in_balance(self.account.name)
        total_accounts, total_loans = report['Oma tili']['Yhteensä'], report['Lainojen lyhennykset']['Yhteensä']
        self.assertEqual(round(total_accounts, 2), -275.01)
        self.assertEqual(round(total_loans, 2), 16547.14)
