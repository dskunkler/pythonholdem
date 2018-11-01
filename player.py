#Player object requires amount of buyin and the players name in constructor 
class Player(object):
    def __init__(self, buyin, name):
        self.chips = buyin
        self.hand = []
        self.name = name
        
    def getHand(self, i):
        self.hand.append(i)
        
    def showHand(self):
        #returns string of hand
        return self.hand

    def placeBet(self):
        print("PLAYER", self.name, "CHIPS:", self.__chips)
        bet = eval(input("How much would you like to bet: "))
        self.chips -= bet
        return bet

    def getName(self):
        return self.name    #Redundant too be deleted
        
    def __repr__(self):
        return self.name + ": " + str(self.chips)
