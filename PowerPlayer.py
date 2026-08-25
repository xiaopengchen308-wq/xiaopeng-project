import random
from player import Player


class PowerPlayer(Player):
    def special_move(self):
        points = random.randint(2, 3)
        self.score += points
        print(self.name, "used POWER DUNK and got", points, "points!")

