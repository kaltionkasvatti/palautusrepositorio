GAME = 4

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):

        if self.m_score1 == self.m_score2:
            return self.equal_scores(self.m_score1)

        elif self.m_score1 >= GAME or self.m_score2 >= GAME:
            difference = self.m_score1 - self. m_score2
            return self.adv_or_win(difference)
            
        else:
            return self.diff_scores(self.m_score1, self.m_score2)

    def adv_or_win(self, diff):
        player = "1" if diff > 0 else "2"
        game = "Advantage player" if abs(diff) == 1 else "Win for player"
        return game + player

    def equal_scores(self, score):
        if score <= 2:
            names = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All"
            }
            return names[score]
        else:
            return "Deuce"

    def diff_scores(self, score1, score2):
        names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return f"{names[score1]}-{names[score2]}"