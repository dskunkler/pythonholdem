from random import shuffle

class Card:
    def __init__(self, num = 1, suit = 'spade'):
        self.__num = num
        self.__suit = suit
        if self.__num == 1:
            self.__num = 'A'
        elif self.__num == 11:
            self.__num = 'J'
        elif self.__num == 12:
            self.__num = 'Q'
        elif self.__num == 13:
            self.__num = 'K'
    
    def get_card(self):
        return '{} {}'.format(self.__num, self.__suit)

class Deck(Card):
    def __init__(self, deck = []):
        Card.__init__(self,num =1, suit = 'spade')
        self.__deck = deck
        self.fill()
    
    def fill(self):
        suits = ['Spade','Heart','Club','Diamond']
        for i in range(1,14):
            for j in suits:
                c1 = Card(i,j)
                self.__deck.append(c1)
                
    def deal_one(self):
        card = self.__deck.pop()
        return card.get_card()
    
    def show_deck(self):
        cards = []
        for i in self.__deck:
            cards.append(i.get_card())
        return cards
    
    def shuffle_deck(self):
        shuffle(self.__deck)
