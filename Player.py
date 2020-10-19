
class Player:

    def __init__(self, playerName = None, balance = 0):
        self.__playerName = playerName
        self.__balance = balance
        self.__lastBet = 0
        self.__currentWinnings = 0
        self.__hand = []
        self.__combinations = []

    def getPlayerName(self):
        return self.__playerName

    def getBalance(self):
        return self.__balance

    def getLastBet(self):
        return self.__lastBet

    def getCurrentWinnings(self):
        return self.__currentWinnings

    def getHand(self):
        return self.__hand

    def changeBalance(self, num):
        self.__balance += num
        return True

    def setLastBet(self, num):
        self.__lastBet = num
        return True

    def addToCurrentWinnings(self,num):
        self.__currentWinnings += num
        return True

    def addCard(self, card):
        self.__hand.append(card)
        return True

    def removeCard(self, card):
        self.__hand.pop(self.__hand.index(card))
        return True

    def getPlayer(self):
        PlayerStr = self.__playerName + " has balance of: " + str(self.__balance) + " his last bet: " + str(self.__lastBet) + " And his hand is currently: \n"

        for i in self.__hand:
            PlayerStr += i + ", "

        return PlayerStr

    def getCombinations(self):
        return self.__combinations

    def setCombinations(self, array):
        self.__combinations = array

    def setHand(self, hand):
        self.__hand = hand

