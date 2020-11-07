from Card import *

class Hand:

    def __init__(self):
        self.__hand = []

    def giveCard(self, card):
        self.__hand.append(card)

    def getHand(self):
        return self.__hand

    def removeHand(self):
        return self.__hand.clear()

    def getCardValuesBySuit(self, suitID):
        cardList = []
        for i in self.__hand:
            if i.getCardSuit() == suitID:
                cardList.append(i.getCardValue())
        return cardList

    def getCardValues(self):
        cardList = []
        for i in self.__hand:
            cardList.append(i.getCardValue())
        return cardList

    def getCardSuits(self):
        cardList = []
        for i in self.__hand:
            cardList.append(i.getCardSuit())
        return  cardList

    def mergeHand(self, list = []):
        self.__hand += list

    def setHand(self, list = []):
        self.__hand = list