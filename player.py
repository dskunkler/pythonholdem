#Player object requires amount of buyin and the players name in constructor 
class Player:
    def __init__(self, buyin, name):
        self.chips = buyin
        self.hand = []
        self.name = name
        self.in_hand = True
        
    def get_hand(self, i):
        self.hand.append(i)
        
    def show_hand(self):
        #returns string of hand
        return self.hand

    def __repr__(self):
        return self.name + ": " + str(self.chips)
