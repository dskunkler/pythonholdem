import hand, player


class Game:
    #contructor requires list of names and buyin amount
    def __init__(self, names, buy_in):
        self.players = []
        self.hand_number = 1
        #create players
        for i in range(0, len(names)):
            self.players.append(player.Player(buy_in, names[i]))
            
    def play(self):
        h = hand.Hand(self.players)
        while (True):
            print("\n----------\nPlaying hand: " + str(self.hand_number))
            self.hand_number += 1
            h.play()
            h.clear()
            #rotates betting and blind order
            h.players = h.players[1:] + h.players[:1]

            
names = ["A","B","C"]

g = Game(names, 2000)


g.play()

    
