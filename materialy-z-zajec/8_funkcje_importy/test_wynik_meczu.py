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

    def test_wygrana_gości(self):
        gole = pobierz_liczbe_goli("0:1")
        self.assertEqual(gole, (0, 1))

    def test_dominacja_gospodarzy(self):
        gole = pobierz_liczbe_goli("12:3")
        self.assertEqual(gole, (12, 3))

    def test_wysoki_remis(self):
        gole = pobierz_liczbe_goli("12:12")
        self.assertEqual(gole, (12, 12))

    def test_dominacja_gosci(self):
        gole = pobierz_liczbe_goli("4:12")
        self.assertEqual(gole, (4, 12))