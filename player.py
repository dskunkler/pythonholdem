#Player object requires amount of buyin and the players name in constructor 
class Player(object):
    def __init__(self, buyin, name):
        self.chips = buyin
        self.hand = []
        self.name = name
        self.inHand = True
        
    def getHand(self, i):
        self.hand.append(i)
        
    def showHand(self):
        #returns string of hand
        return self.hand

    def __repr__(self):
        return self.name + ": " + str(self.chips)
