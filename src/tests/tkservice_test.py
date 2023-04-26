import unittest
from services.tk_service import TKService
from repositories.save_data import save_account
import os

class TestTKService(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.data = os.path.join(dirname, "test_file_short.csv")
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

    def test_print_cashflow_counts_misc_exp_correctly_with_default_value(self):
        self.account.summary(self.data)
        misc1 = self.account.print_cashflow()[2]
        self.assertEqual(round(misc1, 2), 0)

    def test_print_cashflow_counts_misc_exp_correctly_with_set_value(self):
        self.account.summary(self.data)
        misc2 = self.account.print_cashflow(min_exp=2000)[2]
        self.assertEqual(round(misc2, 2), -2449.70)

    def test_print_cashflow_counts_total_money_in_correctly(self):
        self.account.summary(self.data)
        total_money_in = self.account.print_cashflow()[0]
        self.assertEqual(round(total_money_in, 2), 40808.04)

    def test_print_cashflow_counts_total_money_out_correctly(self):
        self.account.summary(self.data)
        total_money_out = self.account.print_cashflow()[1]
        self.assertEqual(round(total_money_out, 2), -38072.33)
   
    def test_print_result_counts_misc_exp_correctly_with_default_value(self):
        self.account.summary(self.data)
        misc1 = self.account.print_result()[2]
        self.assertEqual(round(misc1, 2), 0)

    def test_print_cashflow_counts_misc_exp_correctly_with_set_value(self):
        self.account.summary(self.data)
        misc2 = self.account.print_result(min_exp=2000)[2]
        self.assertEqual(round(misc2, 2), -4449.70)

    def test_print_result_counts_total_income_correctly(self):
        self.account.summary(self.data)
        total_income = self.account.print_result()[0]
        self.assertEqual(round(total_income, 2), 37383.03)

    def test_print_result_counts_total_expense_correctly(self):
        self.account.summary(self.data)
        total_expense = self.account.print_result()[1]
        self.assertEqual(round(total_expense, 2), -18375.21)

    def test_save_account_works(self):
        result = save_account(self.account, self.data, test = True)
        self.assertEqual(result, True)

