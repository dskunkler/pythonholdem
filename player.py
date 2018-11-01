
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
        
    def __repr__(self):
        return self.name + ": " + str(self.__chips)
