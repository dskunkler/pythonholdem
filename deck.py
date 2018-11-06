from random import shuffle

class Card:
    ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    suits = ['Spades','Hearts','Diamonds','Clubs']
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __repr__(self):
        return '{} {}'.format(Card.ranks[self.rank], Card.suits[self.suit])
    
class Deck:
    def __init__(self):
        self.deck = []
        self.fill()
    
    def fill(self):
        for i in range(0,13):
            for j in range(0,4):
                c1 = Card(i,j)
                self.deck.append(c1)
                
    def deal_one(self):
        card = self.deck.pop()
        return card
            
    def shuffle_deck(self):
        shuffle(self.deck)

    def __repr__(self):
        deck_str = ''
        for i in range(0, 49, 4):
            deck_str += '{} {} {} {}\n'.format(self.deck[i], self.deck[i+1],
                                               self.deck[i+2], self.deck[i+3])
        return deck_str
