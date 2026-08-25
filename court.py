import random
from PowerPlayer import PowerPlayer
from quickplayer import QuickPlayer

class Court:
    def __init__(self):
        self.players = [
            PowerPlayer("Lebron"),
            QuickPlayer("Steph"),
            PowerPlayer("Giannis"),
            QuickPlayer("Kyrie")
        ]

    def choose_player(self):
        print("Choose your player:")

        for i in range(len(self.players)):
            print(i + 1, self.players[i].name)

        while True:
            choice = input("Enter 1, 2, 3, or 4: ")

            if choice == "1" or choice == "2" or choice == "3" or choice == "4":
                return self.players[int(choice) - 1]
            else:
                print("Invalid choice. Try again.")

    def play(self):
        player = self.choose_player()

        computer_choices = []

        for p in self.players:
            if p != player:
                computer_choices.append(p)

        computer = random.choice(computer_choices)

        print("You chose", player.name)
        print("Computer chose", computer.name)

        while player.score < 50 and computer.score < 50:

            print("Your score:", player.score)
            print("Computer score:", computer.score)

            print("1. Shoot")
            print("2. Layup")
            print("3. Special Move")

            move = input("Choose your move: ")

            if move == "1":
                player.shoot()

            elif move == "2":
                player.layup()

            elif move == "3":
                player.special_move()

            else:
                print("Invalid move.")
                continue

            if player.score >= 50:
                break

            computer_move = random.randint(1, 3)

            print("Computer's turn:")

            if computer_move == 1:
                computer.shoot()

            elif computer_move == 2:
                computer.layup()

            else:
                computer.special_move()

        print("Final Score")
        print(player.name, ":", player.score)
        print(computer.name, ":", computer.score)

        if player.score >= 50:
            print("You win!")
        else:
            print("Computer wins!")

        if player.name =="Lebron":
            print("Lebron is the goat!!! ")

        if computer.name =="Lebron":
                    print("Lebron is the goat!!! ")
        


game = Court()
game.play()
