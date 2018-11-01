import deck, player

class Game:
    def __init__(self,names,buyin):
        self.players = []
        self.comm = [] #community cards
        self.pot = 0
        self.deck = deck.Deck()
        #create players
        for i in range(0, len(names)):
            self.players.append(player.Player(200, names[i]))

    def bettingPhase(self):
        print("\n", "POT IS: ", self.pot)
        for x in range( len(self.players)):
            self.pot += self.players[x].placeBet()
            

    def play(self):
        self.deck.shuffleDeck()
        #deal
        for x in self.players:
            for i in range(2):
                x.getHand(self.deck.dealOne())

        #pre-flop hands
        self.print_game()
                
        #pre-flop betting round
        self.bettingPhase()

        #flop
        self.community_deal()
        self.print_game()

        #betting round 2
        self.bettingPhase()

        #the turn
        self.community_deal()
        self.print_game()
        
        #betting round 3
        self.bettingPhase()

        #the river
        self.community_deal()
        self.print_game()
        
        #betting round 4 (final)
        self.bettingPhase()
        
    def community_deal(self):
        if (len(self.comm) == 0):
            for i in range(3):
                self.comm.append(self.deck.dealOne())
        elif (len(self.comm) <= 5):
            self.comm.append(self.deck.dealOne())
        else:
            raise RuntimeError("Community cards overflow")

#    def betting(self):
        
    #debugging tool
    def print_game(self):
        print("\nCOMMUNITY CARDS:\n" + "; ".join(self.comm))
        print("PLAYERS")
        for x in self.players:
            print(x)
            print(x.showHand())
            
            
names = ["A","B","C"]

g = Game(names, 200)

g.play()
print(g.players)
