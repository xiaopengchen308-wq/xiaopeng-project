import random
from player import Player

class QuickPlayer(Player):
    def special_move(self):
        points = random.randint(2, 3)
        self.score += points
        print(self.name, "used Quick Shot for", points, "points!")

