import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def shoot(self):
        points = random.randint(2, 3)
        self.score += points
        print(self.name, "made a shot and got", points, "points!")

    def layup(self):
        points = 2
        self.score += points
        print(self.name, "made a layup and got", points, "points!")

