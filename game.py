import hand, player

class Game:
    #contructor requires list of names and buyin amount
    def __init__(self, names, buyin):
        self.players = []
        self.handNumber = 1
        #create players
        for i in range(0, len(names)):
            self.players.append(player.Player(buyin, names[i]))
            
    def play(self):
        h = hand.Hand(self.players)
        while (True):
            print("\n----------\nPlaying hand: " + str(self.handNumber))
            self.handNumber += 1
            h.play()
            h.clear()

            
names = ["A","B","C"]

g = Game(names, 200)

g.play()
