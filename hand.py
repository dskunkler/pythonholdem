import deck
import player

class Hand:
    # Constructor requires list of current players
    def __init__(self,players):
        self.players = players             # List of players
        self.curr_players = len(players)   # Players in current hand
        self.deck = deck.Deck()   
        self.comm = []                     # Community cards

        self.blind = 50 #holds blinds

        self.pot = 0
        self.curr_bet = 0

    def clear(self): #reset hand
        self.curr_players = len(self.players)
        self.deck = deck.Deck()
        self.comm = []

        self.pot = 0
        self.curr_bet = 0

        for player in self.players:
            player.in_hand = True
            player.hand = []
        
    def play(self):
        self.deck.shuffle_deck()

        self.blind_phase() #Posts blinds             

        #deal to players
        for player in self.players:
            for i in range(2):
                player.get_hand(self.deck.deal_one())

        #pre-flop hands
        self.print_game()
        
        #pre-flop betting round
        self.betting_phase()

        #flop, turn, river: community deal and betting phase
        i = 0
        while (i < 3 and self.curr_players > 1):
            self.community_deal()
            self.print_game()
            self.betting_phase()
            i += 1
            
    def betting_phase(self):
        print("\nPOT IS: ", self.pot)

        for player in self.players:
            #give options for players in game, if > 1 player in game
            while (player.in_hand and self.curr_players > 1):
                print("PLAYER", player.name, "CHIPS:", player.chips)

                #still need to add logic on when you can do certain things
                if (self.curr_bet == 0):
                    choice = input("check (c), bet (b), fold (f):\n")
                else:
                    choice = input("call (ca), raise (r), fold (f):\n")

                if choice == "c":
                    break
                elif choice == "b":
                    if (self.place_bet(player)):
                        break
                elif choice == "ca":
                    if (self.call_bet(player)):
                        break
                elif choice == "r":
                    if (self.raise_bet(player)):
                        break
                elif choice == "f":
                    if (self.fold(player)):
                        break

        self.curr_bet = 0  #reset curr_bet for the next round
        
    def blind_phase(self):
        self.pot += self.blind
        self.players[len(self.players)-1].chips -= self.blind
        print("Big Blind", self.players[len(self.players)-1].name, "bet in", self.blind)
        self.pot += self.blind//2
        self.players[len(self.players) -2].chips -= self.blind//2
        print("Little Blind", self.players[len(self.players)-2].name, "bet in", self.blind//2)

    def place_bet(self, player):
        bet = int(input("How much would you like to bet: "))
        if (bet <= player.chips and bet > self.curr_bet):
            print("Placed bet of " + str(bet))
            player.chips -= bet
            self.pot += bet
            self.curr_bet = bet
            return True
        else:
            if (bet > player.chips):
                print("Not enough chips!")
            return False

    def raise_bet(self, player):        
        print("The current bet is: {0}\n".format(self.curr_bet))
        raise_amount = int(input("How much would you like to raise: "))
        total = self.curr_bet + raise_amount
        
        if (raise_amount <= player.chips):
            print("Raised bet to " + str(total))
            player.chips -= total
            self.pot += total
            self.curr_bet = total
            return True

        else:
            if (total > player.chips):
                print("Not enough chips!\n")
            return False
        
    def call_bet(self, player):
        if (self.curr_bet <= player.chips):
            print("Called a bet of " + str(self.curr_bet))
            player.chips -= self.curr_bet
            self.pot += self.curr_bet
            return True
        else:
            print("Not enough chips!\n")
            return False
        
    def fold(self, player):
        player.in_hand = False
        self.curr_players -= 1
        return True
    
    def community_deal(self):
        if (len(self.comm) == 0):
            for i in range(3):
                self.comm.append(self.deck.deal_one())
        elif (len(self.comm) <= 5):
            self.comm.append(self.deck.deal_one())
        else:
            raise RuntimeError("Community cards overflow")
    
    #debugging tool
    def print_game(self):
        print("\nCOMMUNITY CARDS:")
        print(self.comm)
        print("\nPLAYERS:")
        for x in self.players:
            if (x.in_hand == True):
                print(x)
                print(x.show_hand())
            else:
                print(x)
                print("Folded")
