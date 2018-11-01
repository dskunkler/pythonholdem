import deck, player

class Hand:
    def __init__(self,players):
        self.players = players
        self.comm = [] #community cards
        self.pot = 0
        self.deck = deck.Deck()

    def bettingPhase(self):
        print("\n", "POT IS: ", self.pot)
        for x in range(len(self.players)):
            self.pot += self.players[x].placeBet()

    def play(self):
        self.deck.shuffleDeck()

        ###ph-might want to stick in a new method, might not be necessary though
        #deal to players
        for x in self.players:
            for i in range(2):
                x.getHand(self.deck.dealOne())

        #pre-flop hands
        self.printGame()
                
        #pre-flop betting round
        self.bettingPhase()

        #flop, turn, river: community deal and betting phase
        i = 0
        while (i < 3 and self.continueGame()):
            self.communityDeal()
            self.printGame()
            self.bettingPhase()
            i += 1
        
    def communityDeal(self):
        if (len(self.comm) == 0):
            for i in range(3):
                self.comm.append(self.deck.dealOne())
        elif (len(self.comm) <= 5):
            self.comm.append(self.deck.dealOne())
        else:
            raise RuntimeError("Community cards overflow")

    #ph-will be using this to determine whether to cont game
    
    def continueGame(self):
        return True
        
    #debugging tool
    def printGame(self):
        print("\nCOMMUNITY CARDS:\n" + "; ".join(self.comm))
        print("PLAYERS")
        for x in self.players:
            print(x)
            print(x.showHand())
            
            
names = ["A","B","C"]

#this stuff will go into a new "Game" class for the overall game
#but can stay here for current testing
#create players
players = []
for i in range(0, len(names)):
    players.append(player.Player(200, names[i]))

h = Hand(players)

h.play()
print(h.players)
