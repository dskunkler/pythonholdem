"""
Created on Thu Oct 25 11:37:40 2018

@author: Daniel Kujnkler
"""
from random import shuffle


class Card(object):
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
    
    
    
    def getCard(self):
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
                
    def dealOne(self):
        card = self.__deck.pop()
        return card.getCard()
    
    def showDeck(self):
        cards = []
        for i in self.__deck:
            cards.append(i.getCard())
        return cards
    
    def shuffleDeck(self):
        shuffle(self.__deck)
