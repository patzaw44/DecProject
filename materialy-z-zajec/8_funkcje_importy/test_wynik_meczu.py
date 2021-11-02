from unittest import TestCase
from wynik_meczu import pobierz_liczbe_goli


# 1:0 -> (1, 0)
# 0:0 -> (0, 0)
# 1:2 -> (1, 2)
# 12:3 -> (12, 3)
# 11:15 -> (11, 15)
# 4:12 -> (4, 12)

class Test(TestCase):
    def test_wygrana_gospodarzy(self):
        gole = pobierz_liczbe_goli("1:0")
        self.assertEqual(gole, (1, 0))

    def test_remis(self):
        gole = pobierz_liczbe_goli("0:0")
        self.assertEqual(gole, (0, 0))

    def test_wygrana_gosci(self):
        gole = pobierz_liczbe_goli("1:2")
        self.assertEqual(gole, (1, 2))

    def test_dominacja_gospodarzy(self):
        gole = pobierz_liczbe_goli("12:3")
        self.assertEqual(gole, (12, 3))

    def test_wysoki_remis(self):
        gole = pobierz_liczbe_goli("13:13")
        self.assertEqual(gole, (13, 13))

    def test_dominacja_gosci(self):
        gole = pobierz_liczbe_goli("5:17")
        self.assertEqual(gole, (5, 17))

    def test_trzycyfrowy_wynik(self):
        gole = pobierz_liczbe_goli("130:121")
        self.assertEqual(gole, (130, 121))

