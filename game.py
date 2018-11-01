import hand

class Game:
    def __init__(self, names, buyin):
        self.players = []
        #create players
        for i in range(0, len(names)):
            self.players.append(player.Player(buyin, names[i]))

    def play(self):
        h = Hand(players)


names = ["A","B","C"]

g = Game(names, 200)

g.play()
