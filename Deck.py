from Card import *
import random as rnd

class Deck():
    def __init__(self):
        self.__Deck = []
        suits = list(range(4))
        values = list(range(2,15))
        for i in suits:
            for j in values:
                self.__Deck.append(Card(i, j))
        rnd.shuffle(self.__Deck)

    def getDeck(self):
        return self.__Deck

    def getCardFromDeck(self, cardNumber):
        return self.__Deck[cardNumber]

    def deal(self):
        return self.__Deck.pop()


