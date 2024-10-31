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
    
    def test_search_returns_player(self):
        player = self.stats.search("Kurri")
        self.assertAlmostEqual(str(player), f"Kurri EDM 37 + 53 = 90")
    
    def test_player_not_exist(self):
        player = self.stats.search("Anton")
        self.assertAlmostEqual(player, None)

    def test_team_works(self):
        team = self.stats.team("EDM")

        players = []
        for player in team:
            players.append(str(player))

        self.assertListEqual(players, [
            str(Player("Semenko", "EDM", 4, 12)),
            str(Player("Kurri",   "EDM", 37, 53)),
            str(Player("Gretzky", "EDM", 35, 89))
        ])
    
    def test_sort_works(self):
        top = self.stats.top(1)
        
        best = []
        for player in top:
            best.append(str(player))
        
        self.assertListEqual(best,
                               [
            str(Player("Gretzky", "EDM", 35, 89)),
            str(Player("Lemieux", "PIT", 45, 54))
        ])