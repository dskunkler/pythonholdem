
class Player(object):
    def __init__(self, buyin, name):
        self.__chips = buyin
        self.__hand = []
        self.name = name
        
    def getHand(self, i):
        self.__hand.append(i)
        
    def showHand(self):
        #returns string of hand
        return self.__hand

    def placeBet(self):
        print("PLAYER", self.name, "CHIPS:", self.__chips)
        bet = eval(input("How much would you like to bet: "))
        self.__chips -= bet
        return bet

    def getName(self):
        return self.__name
        
    def __repr__(self):
        return self.name + ": " + str(self.__chips)

