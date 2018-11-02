import hand, player

class Game:
    #contructor requires list of names and buyin amount
    def __init__(self, names, buyin):
        self.players = []
        #create players
        for i in range(0, len(names)):
            self.players.append(player.Player(buyin, names[i]))

    def play(self):
        h = hand.Hand(self.players)
        h.play()


names = ["A","B","C"]

g = Game(names, 200)

g.play()
