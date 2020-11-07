import Table as t
import Player as p
import Card as c

newTable = t.Table()
player1 = p.Player("A")
player2 = p.Player("B")


player1.givePlayerChips(100)
player2.givePlayerChips(100)


newTable.addPlayerToTable(player1)
newTable.addPlayerToTable(player2)


print(newTable.getPlayers())
print(newTable.getPlayerByIndex(0).getChips())
print(newTable.getChipPile())


for i in range(4):

    newTable.dealCards()

    print(newTable.getTableHand())

    for i in newTable.getPlayers():
        print(i.getHand())

    for i in newTable.getPlayers():
        print("Talbe: " + str(newTable.getChipPile()))
        betAmt = -1
        while betAmt < newTable.getMaxBet():
            betAmt = 2
            if betAmt >= newTable.getMaxBet():
                betAmt = i.bet(betAmt)
                if betAmt != False:
                    newTable.placeBet(betAmt)
                    newTable.setMaxBet(betAmt)

newTable.checkWin()

