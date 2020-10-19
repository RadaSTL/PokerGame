import random as rnd


def intCast(input):
    try:
        int(input)
        return int(input)
    except ValueError:
        return False
    except:
        raise


class Deck:
    def __init__(self):
        self.__CurrentDeck = []

    def CreateDeck(self):

        faceCards = ["A", "K", "Q", "J"]
        shapes = ["⯁", "♥", "♠", "♣"]
        joker = "Joker"

        for i in range(len(shapes)):
            for j in range(len(faceCards)):
                self.__CurrentDeck.append(shapes[i] + faceCards[j])
            for j in range(2, 11):
                self.__CurrentDeck.append(shapes[i] + str(j))

        rnd.shuffle(self.__CurrentDeck)

        return self.__CurrentDeck

    def giveCard(self):
        card = self.__CurrentDeck[-1]
        self.__CurrentDeck.pop(-1)
        return card

    def getDeck(self):
        DeckStr = "The deck: \n"

        for i in self.__CurrentDeck:
            DeckStr += i + ", "

        return DeckStr

    def getCardValue(self, card):
        cardValue = {"A": 1, "K": 13, "Q": 12, "J": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                     "10": 10, "Joker": 2}
        cardShapes = {"⯁": 9000, "♥": 9100, "♠": 9200, "♣": 9300}
        cardVal = 0
        if card in ["Joker", "2"]:
            cardVal += 1400 + cardValue[card]
        else:
            cardVal += cardValue[card[1:]]
            cardVal += cardShapes[card[0]]
        return cardVal

    def getCardFromValue(self, card):
        cardValue = {"A": 1, "K": 13, "Q": 12, "J": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                     "10": 10, "Joker": 2}
        cardShapes = {"⯁": 9000, "♥": 9100, "♠": 9200, "♣": 9300}
        cardStr = ""

        for key in cardShapes:
            if cardShapes[key] == int(card/100)*100:
                cardStr += key
        for key in cardValue:
            if cardValue[key] == card%100:
                cardStr += key

        return cardStr

