from Table import *
from Player import *


noOfPlayers = int(input("Welcome to Poker Game, please insert number of players: "))

gameTable = Table()
currentPlayerIndex = 0

def isHelpOrReturn(returnInput):
    if (returnInput == "--help"):
        print("1. Royal Flush	10JQKA	The best possible hand in Texas hold'em is the combination of ten, jack, queen, king, ace, all of the same suit\n2. Straight Flush	56789	Five cards of the same suit in sequential order\n3. Four of a kind	3333K	Any four numerically matching cards\n4. Full house	JJJKK	Combination of three of a kind and a pair in the same hand\n5. Flush	2459K	Five cards of the same suit, in any order\n6. Straight	A2345	Five cards of any suit, in sequential order\n7. Three of a kind	77745	Any three numerically matching cards\n8. Two pair	99KK4	Two different pairs in the same hand\n9. One pair	10103QK	Any two numerically matching cards\n10. High card	K248Q	The highest ranked card in your hand with an ace being the highest and two being the lowest")
        returnInput = isHelpOrReturn(input())
    elif (returnInput == "--return"):
        getCurrentStatus()
        returnInput = isHelpOrReturn(input())
    else:
        return str(returnInput)


def getCurrentStatus():

    playerScores = ""

    for player in gameTable.getPlayers():
        if not player.getIsFold():
            if not player.getIsAllIn():
                playerScores += player.getPlayerName() + " has " + str(player.getChips()) + " chips and his last bet is: " + str(player.getPlayerBet()) + "\n"
            else:
                playerScores += player.getPlayerName() + " is all in\n"
        else:
            playerScores += player.getPlayerName() + " has folded\n"

    for player in gameTable.getFoldedPlayers():
        playerScores += player[0].getPlayerName() + " has folded\n"

    print(str(gameTable.getTableHand()) + " Pile: " + str(gameTable.getChipPile()) + " Max bet: " + str(gameTable.getMaxBet()) + "\n" + playerScores)

def gameRound():
    gameTable.startNewRound()
    gameTable.dealCards()
    gameResult = False

    while not gameResult:
        getCurrentStatus()

        for player in gameTable.getPlayers():
            if not player.getIsAllIn() or not player.getIsFold():
                print("It is " + player.getPlayerName() + "'s turn! You have: " + str(player.getHand()) + "\n")
                placedBet = isHelpOrReturn(input("Please place a bet, or write ""--fold"" to fold.\n"))

                if (placedBet == "--fold"):
                    gameTable.foldPlayer(player)
                else:
                    placeBetResult = gameTable.placeBet(player, int(placedBet))
                    while (not placeBetResult):
                        print("It is " + player.getPlayerName() + "'s turn! You have: " + str(player.getHand()) + "\n")
                        placedBet = isHelpOrReturn(input("Please place a bet, or write ""--fold"" to fold.\n"))

                        if (placedBet == "--fold"):
                            gameTable.foldPlayer(player)
                        else:
                            placeBetResult = gameTable.placeBet(player, int(placedBet))

        gameResult = gameTable.checkWin()
        gameTable.dealCards()
    print(str(gameTable.getWinningPlayers()) + " has won!")
    gameTable.payDividents()


while True:
    if noOfPlayers > 6:
        print("Too many players!\n")
        noOfPlayers = int(input("Welcome to Poker Game, please insert number of players: "))
    else:
        break

for i in range(noOfPlayers):
    playerName = input("Please write the name of player " + str(i+1) + ": ")
    gameTable.addPlayerToTable(playerName)
    player = gameTable.getPlayerFromName(playerName)
    player.givePlayerChips(500)

contGame = True


while contGame:
    gameRound()

    contGameStr = isHelpOrReturn(input("New round? Y/N"))
    if contGameStr == "Y":
        contGame = True
    else:
        contGame = False

