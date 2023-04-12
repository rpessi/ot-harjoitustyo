import unittest
from services.tk_service import TKService


class TestTKService(unittest.TestCase):
    def setUp(self):
        self.data = "src/tests/test_file.csv"
        self.account = TKService("Nordea", self.data)

    def test_summary_counts_expenses_correctly(self):
        self.account.summary(self.data)
        key1 = "Helen Oy"
        key2 = "Sipoon Energia Oy"
        self.assertEqual(round(self.account.expense[key1], 2), -763.89)
        self.assertEqual(round(self.account.expense[key2], 2), -1639.25)

    def test_summary_counts_income_correctly(self):
        self.account.summary(self.data)
        key1 = "PESSI RIITTA"
        key2 = "PALKANMAKSAJA"
        self.assertEqual(round(self.account.income[key1], 2), 3050.00)
        self.assertEqual(round(self.account.income[key2], 2), 37383.03)

    def test_print_summary_counts_misc_exp_correctly_with_default_value(self):
        self.account.summary(self.data)
        self.account.print_summary()
        self.assertEqual(round(self.account.total_misc_exp, 2), -800.15)

    def test_print_summary_counts_misc_exp_correctly_with_set_value(self):
        self.account.summary(self.data)
        self.account.print_summary(min_exp=200)
        self.assertEqual(round(self.account.total_misc_exp, 2), -1326.47)
