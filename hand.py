import deck, player

class Hand:
    #constructor requires list of current players
    def __init__(self,players):
        self.players = players            #list of players
        self.currPlayers = len(players)   #players in current hand
        self.deck = deck.Deck()   
        self.comm = []                    #community cards

        self.blind = 50 #holds blinds

        self.pot = 0
        self.currBet = 0

    def clear(self): #reset hand
        self.currPlayers = len(self.players)
        self.deck = deck.Deck()
        self.comm = []

        self.pot = 0
        self.currBet = 0

        for player in self.players:
            player.inHand = True
            player.hand = []
        
    def play(self):
        self.deck.shuffleDeck()

        self.blindPhase() #Posts blinds             

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
        while (i < 3 and self.currPlayers > 1):
            self.communityDeal()
            self.printGame()
            self.bettingPhase()
            i += 1
            
    def bettingPhase(self):
        print("\nPOT IS: ", self.pot)

        for player in self.players:
            #give options for players in game, if > 1 player in game
            while (player.inHand and self.currPlayers > 1):
                print("PLAYER", player.name, "CHIPS:", player.chips)

                #still need to add logic on when you can do certain things
                if (self.currBet == 0):
                    choice = input("check (c), bet (b), fold (f):\n")
                else:
                    choice = input("call (ca), raise (r), fold (f):\n")
                
                if choice == "c":
                    break
                elif choice == "b":
                    if (self.placeBet(player)):
                        break
                elif choice == "ca":
                    if (self.callBet(player)):
                        break
                elif choice == "r":
                    if (self.raiseBet(player)):
                        break
                elif choice == "f":
                    if (self.fold(player)):
                        break
                
        self.currBet = 0  #reset currBet for the next round
        
    def blindPhase(self):
        self.pot += self.blind
        self.players[len(self.players) -1].chips -= self.blind
        print("Big Blind", self.players[len(self.players) -1].name, "bet in", self.blind)
        self.pot += self.blind//2
        self.players[len(self.players) -2].chips -= self.blind//2
        print("Little Blind", self.players[len(self.players) -2].name, "bet in", self.blind//2)

    def placeBet(self, player):
        bet = int(input("How much would you like to bet: "))
        if (bet <= player.chips and bet > self.currBet):
            print("Placed bet of " + str(bet))
            player.chips -= bet
            self.pot += bet
            self.currBet = bet
            return True
        else:
            if (bet > player.chips):
                print("Not enough chips!")
            return False

    def raiseBet(self, player):        
        print("The current bet is: {0}\n".format(self.currBet))
        raiseAmount = int(input("How much would you like to raise: "))
        total = self.currBet + raiseAmount
        
        if (raiseAmount <= player.chips):
            print("Raised bet to " + str(total))
            player.chips -= total
            self.pot += total
            self.currBet = total
            return True

        else:
            if (total > player.chips):
                print("Not enough chips!\n")
            return False
        
    def callBet(self, player):
        if (self.currBet <= player.chips):
            print("Called a bet of " + str(self.currBet))
            player.chips -= self.currBet
            self.pot += self.currBet
            return True
        else:
            print("Not enough chips!\n")
            return False
        
    def fold(self, player):
        player.inHand = False
        self.currPlayers -= 1
        return True
    
    def communityDeal(self):
        if (len(self.comm) == 0):
            for i in range(3):
                self.comm.append(self.deck.dealOne())
        elif (len(self.comm) <= 5):
            self.comm.append(self.deck.dealOne())
        else:
            raise RuntimeError("Community cards overflow")
    
    #debugging tool
    def printGame(self):
        print("\nCOMMUNITY CARDS:\n" + "; ".join(self.comm))
        print("\nPLAYERS:")
        for x in self.players:
            print(x)
            print(x.showHand())
