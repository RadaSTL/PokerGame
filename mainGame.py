from Table import *

testTable = Table()

testTable.CreateTable(5,2,10,100,1000)

playerList = testTable.getPlayerList()

testTable.dealToPlayers()

testTable.dealToTable()
testTable.dealToTable()
testTable.dealToTable()
testTable.dealToTable()
testTable.dealToTable()



print(testTable.getWinner())
