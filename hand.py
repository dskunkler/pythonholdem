import deck, player

class Hand:
    #constructor requires list of current players
    def __init__(self,players):
        self.players = players #list of players
        self.deck = deck.Deck()
        self.comm = [] #community cards

        self.pot = 0
        self.currBet = 0

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
        
    def bettingPhase(self):
        print("\nPOT IS: ", self.pot)

        for player in self.players:
            while (True):
                print("PLAYER", player.name, "CHIPS:", player.chips)

                #still need to add logic on when you can do certain things
                choice = input("check, bet, call, raise, fold:\n")
                if choice == "check":
                    break
                elif choice == "bet":
                    self.placeBet(player)
                    break
                elif choice == "call":
                    self.callBet(player)
                    break
                elif choice == "fold":
                    self.fold(player)
                    break
                    
    def placeBet(self, player):
        bet = int(input("How much would you like to bet: "))
        if (bet <= player.chips):
            print("Placed bet of " + str(bet))
            player.chips -= bet
            self.pot += bet
            self.currBet = bet
            return True
        else:
            print("Not enough chips")
            return False

    def callBet(self, player):
        if (self.currBet <= player.chips):
            print("Called a bet of " + str(self.currBet))
            player.chips -= self.currBet
            self.pot += self.currBet
            return True
        else:
            return False
        
    def fold(self, player):
        player.inHand = False
        return True
            
    def communityDeal(self):
        if (len(self.comm) == 0):
            for i in range(3):
                self.comm.append(self.deck.dealOne())
        elif (len(self.comm) <= 5):
            self.comm.append(self.deck.dealOne())
        else:
            raise RuntimeError("Community cards overflow")

    #ph-will be using this to determine whether to cont game
    #with >= 2 players in game basically
    def continueGame(self):
        return True
        
    #debugging tool
    def printGame(self):
        print("\nCOMMUNITY CARDS:\n" + "; ".join(self.comm))
        print("\nPLAYERS:")
        for x in self.players:
            print(x)
            print(x.showHand())
