"""
Created on Thu Oct 25 11:37:40 2018

@author: Daniel Kujnkler
"""
from random import shuffle

class Card(object):
    def __init__(self, num = 1, suit = 'spade'):
        self.__num = num
        self.__suit = suit
    
    def getCard(self):
        return self.__num, self.__suit



class Deck(Card):
    def __init__(self, deck = []):
        Card.__init__(self,num =1, suit = 'spade')
        self.__deck = deck
        self.fill()
    
    def fill(self):
        suits = ['spade','heart','club','diamond']
        for i in range(1,14):
            for j in suits:
                c1 = Card(i,j)
                self.__deck.append(c1.getCard())
                
    def dealOne(self):
        return self.__deck.pop()  
    
    def showDeck(self):
        return self.__deck
    
    def shuffleDeck(self):
        shuffle(self.__deck)