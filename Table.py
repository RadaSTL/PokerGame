from Player import *
from Deck import *

class Table(Deck, Player):
    def __init__(self):
        Player.__init__(self)
        Deck.__init__(self)
        self.__playerList = {}
        self.__playDeck = Deck()
        self.__minBet = 0
        self.__maxBet = 0
        self.__minEntrance = 0
        self.__tablePile = []
        self.__bestHands = {}

    def getTableCards(self):
        return self.__tablePile

    def getPlayerFromList(self, player):

        return self.__playerList[player].getPlayer()

    def getPlayerList(self):
        return self.__playerList

    def getPlayerListInfo(self):
        strPlayerList = "Current Players on the table:\n"
        for i in self.__playerList:
            strPlayerList += self.__playerList[i].getPlayer() + "\n"

        return strPlayerList

    def getDeck(self):
        return self.__playDeck.getDeck()

    def CreateTable(self, playerCount = 2, minBet = 0, maxBet = 10, minEntrance = 100, defaultBalance = 1000):
        self.__minBet = minBet
        self.__maxBet = maxBet
        self.__minEntrance = minEntrance
        self.__playDeck.CreateDeck()
        for i in range(playerCount):
            playerName = input("Please enter name of player " + str(i+1) + ": ")
            self.__playerList[playerName] = Player(playerName,defaultBalance)
        return True

    def dealToTable(self):
        self.__tablePile.append(self.__playDeck.giveCard())

    def dealToPlayers(self):
        for i in self.__playerList:
            self.__playerList[i].addCard(self.__playDeck.giveCard())
            self.__playerList[i].addCard(self.__playDeck.giveCard())
        return True

    """
    12 - Royal Flush
    11 - Stright Flush
    10 - Four House
    9 - Full House
    8 - Flush
    7 - Straight
    6 - Three of a Kind
    4 - Two Pairs
    1 - One Pair
    """

    def calculatePlayerCombinations(self):
        playerCombs = {}
        for i in self.__playerList:
            tempArr = []
            tempArr2 = self.__playerList[i].getHand()
            for y in tempArr2:
                tempArr.append(Deck.getCardValue(self,y))
            for y in self.__tablePile:
                tempArr.append(Deck.getCardValue(self,y))
            playerCombs[i] = {"TempDeck":tempArr}
            playerCombs[i]["Combinatios"] = []

        for player in playerCombs:
            tempArr = playerCombs[player]["TempDeck"]
            tempDict = {}

            for card in tempArr:
                if card in tempDict:
                    tempDict[card] += 1
                else:
                    tempDict[card] = 1
                if card%100 in tempDict:
                    tempDict[card%100] += 1
                else:
                    tempDict[card % 100] = 1
                if int(card/100) in tempDict:
                    tempDict[int(card/100)] += 1
                else:
                    tempDict[int(card/100)] = 1

            for key in tempDict:
                combType = -1
                sameColor = None
                domColor = None
                isStraight = None
                handType = 0
                tempArr2 = []
                pairVal = 0
                if tempDict[key] > 1:
                    if key > 999:
                        for i in range(tempArr.count(key)):
                            tempArr2.append(key)
                        sameColor = False
                        isStraight = False
                    elif key > 50:
                        sortCnt = 0
                        prevKey = -1
                        cnt = 0
                        for i in tempArr:
                            if key == int(i/100):
                                tempArr2.append(i)
                        tempArr2.sort()
                        for i in tempArr2:
                            if cnt > 0 and i - prevKey == 1:
                                sortCnt += 1
                            prevKey = i
                            cnt += 1
                        if sortCnt >= 4:
                            isStraight = True
                        sameColor = True
                        domColor = key
                        if isStraight == True and tempArr2[-1]%100 != 13:
                            handType = 11
                        elif isStraight == True:
                            handType = 12
                        elif len(tempArr2) == 5:
                            handType = 8
                    else:
                        for i in tempArr:
                            if i%100 == key:
                                tempArr2.append(i)
                        if len(tempArr2) == 2:
                            handType = 1
                        if len(tempArr2) == 3:
                            handType = 6
                        if len(tempArr2) == 4:
                            handType = 10
                        pairVal = tempArr2[0]%100
                        isStraight = False
                        sameColor = False
                if len(tempArr2) > 0 and handType > 0:
                    playerCombs[player]["Combinatios"].append(
                        {
                            "CombArr": tempArr2,
                            "CombType": handType,
                            "isSameColor": sameColor,
                            "Color": domColor,
                            "isStraight": isStraight,
                            "pairValue":pairVal
                        }
                    )
            combType = -1
            sameColor = None
            domColor = None
            isStraight = None
            handType = 0
            tempArr2 = []
            tempArr3 = []
            for i in tempArr:
                tempArr3.append(i%100)
            tempArr3.sort()
            prevIndex = -1
            cnt = 0
            sortCnt = 0
            for y in tempArr:
                if tempArr3[0] == y % 100 and tempArr3.count(y%100) == 1:
                    tempArr2.append(y)
            for i in tempArr3:
                if cnt > 0 and i - prevIndex == 1:
                    for y in tempArr:
                        if i == y%100:
                            tempArr2.append(y)
                    sortCnt += 1
                prevIndex = i
                cnt += 1
            if sortCnt >= 5:
                isStraight = True
                sameColor = False
                handType = 7
            if len(tempArr2) > 0 and handType > 0:
                playerCombs[player]["Combinatios"].append(
                    {
                        "CombArr": tempArr2,
                        "CombType": handType,
                        "isSameColor": sameColor,
                        "Color": domColor,
                        "isStraight": isStraight,
                        "pairValue": pairVal
                    }
                )

        bestHandDic = {}
        for player in self.__playerList:
            bestHandDic[player] = {"Hand":[], "handType":[], "maxVal":0}
            maxVal = -1
            combType = -1

            while len(bestHandDic[player]["Hand"]) < 5:
                for comb in playerCombs[player]["Combinatios"]:
                    if combType < comb["CombType"]:
                        combType = comb["CombType"]
                    if maxVal < comb["pairValue"]:
                        maxVal = comb["pairValue"]

                if len(playerCombs[player]["Combinatios"]) <= 0:
                    bestHandDic[player]["Hand"].append(max(playerCombs[player]["TempDeck"]))
                else:
                    for comb in playerCombs[player]["Combinatios"]:
                        if combType == comb["CombType"] and combType > 1:
                            for card in comb["CombArr"]:
                                bestHandDic[player]["Hand"].append(card)
                            bestHandDic[player]["handType"].append(combType)
                            if bestHandDic[player]["maxVal"] < maxVal:
                               bestHandDic[player]["maxVal"] = maxVal
                        elif maxVal == comb["pairValue"]:
                            for card in comb["CombArr"]:
                                bestHandDic[player]["Hand"].append(card)
                            bestHandDic[player]["handType"].append(combType)
                            if bestHandDic[player]["maxVal"] < maxVal:
                               bestHandDic[player]["maxVal"] = maxVal

                maxVal = -1
                combType = -1

                for comb in playerCombs[player]["Combinatios"]:
                    for cards in comb["CombArr"]:
                        if cards in bestHandDic[player]["Hand"]:
                            try:
                                playerCombs[player]["Combinatios"].pop(playerCombs[player]["Combinatios"].index(comb))
                            except:
                                continue
                for cards in playerCombs[player]["TempDeck"]:
                    if cards in bestHandDic[player]["Hand"]:
                        try:
                            playerCombs[player]["TempDeck"].pop(playerCombs[player]["TempDeck"].index(cards))
                        except:
                            continue
                if bestHandDic[player]["handType"].count(1) >= 2:
                    for i in range(bestHandDic[player]["handType"].count(1)):
                        bestHandDic[player]["handType"].pop(bestHandDic[player]["handType"].index(1))
                    bestHandDic[player]["handType"].append(4)
            if len(bestHandDic[player]["handType"]) == 0:
                bestHandDic[player]["handType"].append(0)


        self.__bestHands = bestHandDic

    def getWinner(self):
        self.calculatePlayerCombinations()
        cnt = 0
        highPlayer = ""
        highScore = -1
        highVal = -1
        highPlayers = []
        for player in self.__bestHands:
            if cnt == 0:
                highPlayer = player
                highScore = self.__bestHands[player]["handType"][0]
                highVal = self.__bestHands[player]["maxVal"]
            elif highScore < self.__bestHands[player]["handType"][0]:
                highPlayer = player
                highScore = self.__bestHands[player]["handType"][0]
                highVal = self.__bestHands[player]["maxVal"]
            elif highScore == self.__bestHands[player]["handType"][0]:
                if self.__bestHands[player]["handType"][0] not in [12,11]:
                    if highVal < self.__bestHands[player]["maxVal"]:
                        highPlayer = player
                        highScore = self.__bestHands[player]["handType"][0]
                        highVal = self.__bestHands[player]["maxVal"]
                elif highVal < self.__bestHands[player]["maxVal"]:
                        highPlayers.append(highPlayer)
                        highPlayers.append(player)
            else:
                highPlayers.append(highPlayer)
                highPlayers.append(player)
        if len(highPlayers) > 0:
            return highPlayers
        else:
            return highPlayer




        print(self.__bestHands)





"""
    def CheatHand(self):
        tempArr = [9010,9110,9210,9310,9013]
        tempArr2 = []
        for i in tempArr:
            tempArr2.append(Deck.getCardFromValue(self,i))
        self.__playerList["a"].setHand(tempArr2)
"""