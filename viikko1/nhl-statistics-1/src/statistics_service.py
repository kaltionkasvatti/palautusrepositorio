from player_reader import PlayerReader
from enum import Enum


class StatisticsService:
    def __init__(self, io):
        
        self._players = io.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sortkey = 1):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(player):
            return player.points

        def sort_by_goals(player):
            return player.goals
        
        def sort_by_assists(player):
            return player.assists
        
        if sortkey == SortBy.GOALS:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_goals
                )
        elif sortkey == SortBy.ASSISTS:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_assists
                )
        else:
            sorted_players = sorted(
                self._players,
                reverse=True,
                key=sort_by_points
                )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3