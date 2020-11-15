from Hand import *

class Player(Hand):

    def __init__(self, Name=None):
        super().__init__()
        self.__name = Name
        self.__chips = 0
        self.__hand = Hand()
        self.__isAllIn = False
        self.__isFold = False

    def __repr__(self):
        return self.__name

    def getChips(self):
        return self.__chips

    def getPlayerName(self):
        return self.__name

    def getPlayerBet(self):
        return self.__name

    def givePlayerChips(self, chipAmnt):
        self.__chips += chipAmnt

    def getIsFold(self):
        return self.__isFold

    def setIsFold(self, bool = False):
        self.__isFold = bool

    def getIsAllIn(self):
        return self.__isAllIn

    def bet(self, chipAmnt):
        if chipAmnt <= self.__chips:
            if chipAmnt == self.__chips:
                self.__isAllIn = True
            self.givePlayerChips(chipAmnt*-1)
            return chipAmnt
        else:
            return False