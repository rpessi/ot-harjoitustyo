import unittest
from services.tk_service import TKService
from repositories.save_data import save_account
import os

class TestTKService(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.data = os.path.join(dirname, "test_file_short.csv")
        self.account = TKService("TEST", self.data)
        self.account.splits['NORDEA LAINAT/LÅN'] = -2000.0
        self.account.offset_account_in['PALKKA'] = ['Tulot']
        self.account.offset_account_in['PESSI RIITTA'] = ['Oma tili']
        self.account.offset_account_in['MJUK GROUP AB'] = ['Menot']
        self.account.offset_account_out['NORDEA LAINAT/LÅN'] = ['Lainat']
        self.account.offset_account_out['Asunto Oy Helsingin Välimeri'] = ['Menot']
        self.account.offset_account_out['NORDEA RAHOITUS SUOMI OY'] = ['Menot']
        self.account.offset_account_out['IF VAKUUTUS'] = ['Menot']
        self.account.offset_account_out['Elisa Oyj'] = ['Menot']

    def test_summary_counts_expenses_correctly(self):
        self.account.summary(self.data)
        key1 = "NORDEA RAHOITUS SUOMI OY"
        key2 = "IF VAKUUTUS"
        self.assertEqual(round(self.account.money_out[key1], 2), -8129.21)
        self.assertEqual(round(self.account.money_out[key2], 2), -1909.96)

    def test_summary_counts_income_correctly(self):
        self.account.summary(self.data)
        key1 = "PESSI RIITTA"
        key2 = "PALKKA"
        self.assertEqual(round(self.account.money_in[key1], 2), 3150.00)
        self.assertEqual(round(self.account.money_in[key2], 2), 37383.03)

    def test_print_summary_counts_misc_exp_correctly_with_default_value(self):
        self.account.summary(self.data)
        misc1 = self.account.print_summary()
        self.assertEqual(round(misc1, 2), 0)

    def test_print_summary_counts_misc_exp_correctly_with_set_value(self):
        self.account.summary(self.data)
        misc2 = self.account.print_summary(min_exp=2000)
        self.assertEqual(round(misc2, 2), -2449.70)

    def check_file_path(self):
        self.assertEqual(self.data, "mikä tähän tulis")

    def test_save_account(self):
        dirname = os.path.dirname(__file__)
        save_account(self.account, test = True)
        #tarvitaan offset.accounts inittiin
        #tarvitaan splits inittiin

        pass
        #
    

