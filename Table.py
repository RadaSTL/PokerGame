from Hand import *
import Player as p
import math as m
import Deck as d
import Card as c

class Table(Hand):

    def __init__(self):
        super().__init__()
        self.__hand = Hand()
        self.__players = []
        self.__chipsPile = 0
        self.__dealerHole = 0
        self.__newDeck = d.Deck()
        self.__roundCount = 0
        self.__maxBet = 0
        self.__winnerCount = 0
        self.__winningPlayers = []

    def getTableHand(self):
        return self.__hand.getHand()

    def getPlayers(self):
        return self.__players

    def getPlayerByIndex(self, index):
        return self.__players[index]

    def getChipPile(self):
        return self.__chipsPile

    def getMaxBet(self):
        return self.__maxBet

    def getPlayerFromName(self,name):
        for i in self.__players:
            if i.getPlayerName() == name:
                return i

    def setMaxBet(self, bet):
        self.__maxBet = bet

    def addPlayerToTable(self, player):
        self.__players.append(player)

    def placeBet(self, bet):
        self.__chipsPile += bet

    def payDividents(self):

        dividentAmount = int(m.floor(self.__chipsPile/self.__winnerCount))

        for i in self.__winningPlayers:
            i.givePlayerChips(dividentAmount)
            self.__chipsPile -= dividentAmount

        self.__chipsPile = 0

    def reassignDealerHole(self):
        self.__dealerHole += 1

        if self.__dealerHole not in range(len(self.__players)):
            self.__dealerHole = 0

    def startNewRound(self):
        self.__chipsPile = 0
        self.__newDeck = d.Deck
        for i in self.__players:
            i.removeHand()
        self.__hand.removeHand()
        self.__roundCount = 0
        self.__dealerHole += 1
        self.__maxBet = 0
        self.__winnerCount = 0
        self.__winningPlayers = []

    def dealCards(self):
        if self.__roundCount == 0:
            for j in range(2):
                for i in range(self.__dealerHole+1, len(self.__players)):
                    self.__players[i].giveCard(self.__newDeck.deal())
                for i in range(self.__dealerHole+1):
                    self.__players[i].giveCard(self.__newDeck.deal())
                self.__hand.giveCard(self.__newDeck.deal())
        elif len(self.__hand.getHand()) <= 5:
            self.__hand.giveCard(self.__newDeck.deal())
        self.__roundCount += 1
        self.__maxBet = 0

    """
    Point Calculation:
    None - ... High -> Point of Highest Card (e.g. if Player has ♣10 as highest card meaning he has 
    10-High, his point will be 10)
    One Pair - Point of the card pair + 1000 (e.g. if player has 10 Pair, the point will be set as 1010)
    Two Pair - Highest card pairs + 2000 (e.g. if player has 10 Pair and 6 Pair, score will be 2010)
    Three of a Kind - Point of ToK + 3000 (e.g. 10 ToK + 3000 will be 3010)
    Straight - 4000 + Highest Card Val
    Flush - 5000  + Highest Card Val
    Full-House - 6000 + ToK Card Val
    Four of a Kind - 7000 + Card Val
    Straight Flush - 8000 + Highest Card Val
    Royal Flush - 9000
    """

    def checkWin(self):
        playerPoints = []
        playerDict = {}
        tempList = Hand()
        if len(self.__hand.getHand()) == 5:
            for i in self.__players:
                tempList = i
                tempList.mergeHand(self.__hand.getHand())
                #tempList.setHand([c.Card(0,2),c.Card(1,3),c.Card(2,4),c.Card(2,5),c.Card(2,6),c.Card(3,7),c.Card(3,9)])
                print(tempList.getHand())
                playerDict[i.getPlayerName()] = 0
                isStraightFlush = False

                for j in range(4):
                    StartsWithAce = False
                    streakCount = 0
                    suitArray = tempList.getCardValuesBySuit(j)
                    suitArray.sort()
                    streakStarter = 0
                    streakEnd = 0

                    for l in range(len(suitArray)):
                        if streakCount < 4:
                            if l == 0 and suitArray[l] == 2 and suitArray[-1] == 14:
                                streakCount += 1
                                if streakCount == 1:
                                    streakStarter = suitArray[l]-1
                                StartsWithAce = True
                                streakEnd = suitArray[l]
                            elif suitArray[l] == suitArray[l-1] + 1:
                                streakCount += 1
                                if streakCount == 1:
                                    streakStarter = suitArray[l]-1
                                streakEnd = suitArray[l]
                            else:
                                if l == len(suitArray) - 1 and StartsWithAce:
                                    pass
                                else:
                                    streakCount = 0

                    if StartsWithAce:
                        streakEnd = 14

                    if streakCount >= 4:
                        if streakStarter == 10:
                            playerDict[i.getPlayerName()] = 9000+streakEnd
                            isStraightFlush = True
                        else:
                            playerDict[i.getPlayerName()] = 8000+streakEnd
                            isStraightFlush = True

                kindsList = i.getCardValues()
                kindsList.sort()
                kindsDic = {}
                for j in kindsList:
                    if j not in kindsDic:
                        kindsDic[j] = 1
                    else:
                        kindsDic[j] += 1

                print(kindsList)
                print(kindsDic)
                ToKPoint = 0
                PairCount = 0
                TPPoint = 0
                for keys in kindsDic:
                    if kindsDic[keys] == 4:
                        playerDict[i.getPlayerName()] = 7000 + keys
                        StartsWithAce = True
                        break
                    if kindsDic[keys] == 3:
                        if 3000+keys > ToKPoint:
                            ToKPoint = 3000+keys
                    if kindsDic[keys] == 2:
                        PairCount += 1
                        if 1000+keys > TPPoint:
                            TPPoint = 1000+keys

                if ToKPoint > 3000 and TPPoint > 1000:
                    playerDict[i.getPlayerName()] = 6000 + ToKPoint%1000
                elif ToKPoint > 3000:
                    playerDict[i.getPlayerName()] = ToKPoint
                elif TPPoint > 1000 and PairCount > 1:
                    playerDict[i.getPlayerName()] = TPPoint + 1000
                elif TPPoint > 1000:
                    playerDict[i.getPlayerName()] = TPPoint


                if not isStraightFlush:
                    streakCount = 0
                    streakStarter = 0
                    streakEnd = 0
                    checkList = i.getCardSuits()
                    checkList.sort()
                    checkDic = {}
                    StartsWithAce = False

                    for j in checkList:
                        if j not in checkDic:
                            checkDic[j] = 1
                        else:
                            checkDic[j] += 1

                    for keys in checkDic:
                        if checkDic[keys] >= 5:
                            suitArray = i.getCardValuesBySuit(keys)
                            suitArray.sort()

                            if playerDict[i.getPlayerName()] < 5000 + suitArray[-1]:
                                playerDict[i.getPlayerName()] = 5000 + suitArray[-1]

                    for l in range(len(kindsList)):
                        if streakCount < 4:
                            if l == 0 and kindsList[l] == 2 and kindsList[-1] == 14:
                                streakCount += 1
                                if streakCount == 1:
                                    streakStarter = kindsList[l] - 1
                                StartsWithAce = True
                                streakEnd = kindsList[l]
                            elif kindsList[l] == kindsList[l - 1] + 1:
                                streakCount += 1
                                if streakCount == 1:
                                    streakStarter = kindsList[l] - 1
                                streakEnd = kindsList[l]
                            else:
                                if l == len(kindsList) - 1 and StartsWithAce:
                                    pass
                                else:
                                    streakCount = 0

                    if StartsWithAce:
                        streakEnd = 14

                    if streakCount >= 4:
                        if playerDict[i.getPlayerName()] < 4000 + kindsList[-1]:
                            playerDict[i.getPlayerName()] = 4000+streakEnd

                if playerDict[i.getPlayerName()] == 0:
                    playerDict[i.getPlayerName()] = kindsList[-1]

        maxPts = 0
        for keys in playerDict:
            if playerDict[keys] > maxPts:
                maxPts = playerDict[keys]

        for keys in playerDict:
            if playerDict[keys] == maxPts:
                self.__winningPlayers.append(self.getPlayerFromName(keys))
                self.__winnerCount += 1


        print(playerDict)
        print(self.__winningPlayers)






