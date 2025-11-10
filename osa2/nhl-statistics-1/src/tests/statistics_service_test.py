import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_etsii_pelaajan(self):
        pelaaja = self.stats.search("Lemieux")
        self.assertEqual(str(pelaaja), "Lemieux PIT 45 + 54 = 99")

    def test_etsii_olemattoman(self):
        pelaaja = self.stats.search("joku")
        self.assertEqual(pelaaja, None)

    def test_listaa_joukkueen(self):
        pelaajat = self.stats.team("EDM")
        self.assertEqual(len(pelaajat), 3)

    def test_palauttaa_ekan(self):
        eka = self.stats.top(1)
        self.assertEqual(str(eka[0]), "Gretzky EDM 35 + 89 = 124")

