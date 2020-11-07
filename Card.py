class Card:
    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value

    def getCard(self):
        return Card

    def getCardValue(self):
        return self.__value

    def getCardSuit(self):
        return self.__suit

    def __repr__(self):
        suit = ""
        value = ""
        if self.__suit == 0:
            suit = "⯁"
        elif self.__suit == 1:
            suit = "♥"
        elif self.__suit == 2:
            suit = "♠"
        elif self.__suit == 3:
            suit = "♣"

        if self.__value <= 10:
            value = str(self.__value)
        elif self.__value == 11:
            value = "J"
        elif self.__value == 12:
            value = "Q"
        elif self.__value == 13:
            value = "K"
        elif self.__value == 14:
            value = "A"

        return suit + value

