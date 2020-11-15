from tkinter import *
from tkinter.font import *
import socket
import subprocess
import threading as th
from Table import *
from Player import *
import pygubu


gameTable = Table()

root = Tk()

root.title("Poker Game")

def createPlayer(btn = Button, entry = Entry, chips = Label, string = None, bet = Entry, betBtn = Button, allIn = Button, fold = Button, getChips = Button):
    if len(string) != 0:
        player = Player(string)
        gameTable.addPlayerToTable(player)
        btn['state']=DISABLED
        entry['state']=DISABLED
        givePlayerChips(chips, string)
        bet['state'] = NORMAL
        betBtn['state'] = NORMAL
        allIn['state'] = NORMAL
        fold['state'] = NORMAL
        getChips['state'] = NORMAL
        dealerStr.set("Dealer: " + gameTable.getDealerPlayer())
    else:
        raise Exception('Error playername is empty')

def givePlayerChips(chipsLbl = Label, playerName = None):
    if playerName != None and playerName != "":
        player = gameTable.getPlayerFromName(playerName)
        if player.getChips() <= 0:
            plChips = player.getChips()
            player.givePlayerChips(100-plChips)
            plChips = player.getChips()
            chipsLbl['text'] = 'Chips: ' + str(plChips)

def btnBet(chips = Label, betEnty = Entry ,playerEntry = Entry):
    Playerbet = int(betEnty.get())
    playerName = playerEntry.get()
    player = gameTable.getPlayerFromName(playerName)
    playerchips = player.getChips()
    if playerchips >= Playerbet:
        betBool = gameTable.placeBet(player, Playerbet)
        if betBool:
            playerchips = player.getChips()
            chips['text'] = 'Chips: ' + str(playerchips)
            tableChipsStr.set("Chips: " + str(gameTable.getChipPile()))

def btnAllIn(chips = Label, betEnty = Entry ,playerEntry = Entry, betBtn = Button, allIn = Button, fold = Button, strVar = StringVar):
    playerName = playerEntry.get()
    player = gameTable.getPlayerFromName(playerName)
    playerchips = player.getChips()
    strVar.set(str(playerchips))
    btnBet(chips, betEnty, playerEntry)
    betBtn['state'] = DISABLED
    allIn['state'] = DISABLED
    fold['state'] = DISABLED
    betEnty['state'] = DISABLED
    tableChipsStr.set("Chips: " + str(gameTable.getChipPile()))


def btnFold(betEnty = Entry ,playerEntry = Entry, betBtn = Button, allIn = Button, fold = Button):
    playerName = playerEntry.get()
    player = gameTable.getPlayerFromName(playerName)
    gameTable.foldPlayer(player)
    betBtn['state'] = DISABLED
    allIn['state'] = DISABLED
    fold['state'] = DISABLED
    betEnty['state'] = DISABLED


gameFrame = Frame (root, height = 600, width = 300)

radPick = IntVar()
radPick.set(0)

def radioPicked(number):
    radPick.set(number)
    if number == 1:
        IP_L['text'] = socket.gethostbyname(socket.gethostname())
        Connect_Entry['state']=NORMAL
        Connect_Button['state'] = NORMAL
    if number == 0:
        IP_L['text'] = " "
        Connect_Entry['state'] = DISABLED
        Connect_Button['state'] = DISABLED

def connectGame():
    pass


singlePlayer = Radiobutton(gameFrame, text="Local Multiplayer", variable=radPick, value=0,
                           command= lambda: radioPicked(0))
multiPlayer = Radiobutton(gameFrame, text="LAN Multiplayer", variable=radPick, value=1,
                          command= lambda: radioPicked(1))

singlePlayer.grid(row=1,columnspan = 2, padx= 20)
multiPlayer.grid(row=2,columnspan = 2, padx = 20)

playerDetailsFrame = LabelFrame(gameFrame, text="Player Name")
playerNameEntry = Entry(playerDetailsFrame)

playerNameEntry.pack(padx=5, pady=5)
playerDetailsFrame.grid(row=0,columnspan=2)

multiPlayerFrame = LabelFrame(gameFrame, text="LAN Settings")

IP_LF = LabelFrame(multiPlayerFrame, text="LAN IP")
IP_L = Label(IP_LF, text=" ")

IP_L.pack()
IP_LF.grid(row=0, columnspan=2, padx=5, pady=5)

Connect_LF = LabelFrame(multiPlayerFrame, text="Find a game:")
Connect_Entry = Entry(Connect_LF, state=DISABLED)
Connect_Button = Button(Connect_LF, text="Connect!", command=connectGame, state=DISABLED)

Connect_Entry.pack(padx=10, pady=10)
Connect_Button.pack(padx=5, pady=5)
Connect_LF.grid(row=1, columnspan=2, padx=5, pady=5)

labelFont = Font(size = 20)
newCard = c.Card(2,0)

mainGame = Frame(root, bg="Green", height=600, width=600)

playerFrameP1 = Frame(mainGame, width=200, height=100, borderwidth=2)

strVarP1 = StringVar()

playerLabelP1 = Label(playerFrameP1, text="Name")
playerNameP1 = Entry(playerFrameP1)
cardFrameP1 = Frame(playerFrameP1, bg="green")
setNameBtnP1 = Button(playerFrameP1, text="Join", command= lambda: createPlayer(playerNameP1, setNameBtnP1, playerChipsP1, playerNameP1.get(),playerBetP1, betButtonP1, allInButtonP1, foldButtonP1, getChipsButtonP1))
playerChipsP1 = Label(playerFrameP1, text="Chips: ")
getChipsButtonP1 = Button(playerFrameP1, text="Get Chips", command= lambda: givePlayerChips(playerChipsP1, playerNameP1.get()), state=DISABLED)
playerBetP1 = Entry(playerFrameP1, state=DISABLED, textvariable=strVarP1)
betButtonP1 = Button(playerFrameP1, text="Bet", state=DISABLED, command= lambda: btnBet(playerChipsP1,playerBetP1,playerNameP1))
allInButtonP1 = Button(playerFrameP1, text="All In", state=DISABLED, command= lambda: btnAllIn(playerChipsP1, playerBetP1, playerNameP1, betButtonP1, allInButtonP1, foldButtonP1, strVarP1))
foldButtonP1 = Button(playerFrameP1, text="Fold", state=DISABLED, command=lambda: btnFold(playerBetP1,playerNameP1, betButtonP1, allInButtonP1, foldButtonP1))

emptyLabelP1 = Label(playerFrameP1, text ="    ")

playerCardP1_1 = Label(cardFrameP1, padx=10, pady=15, bg="White", text=newCard, fg=newCard.getCardColor(), font=labelFont, borderwidth=2, relief="groove")

playerCardP1_2 = Label(cardFrameP1, padx=10, pady=15, bg="White", text=newCard, fg=newCard.getCardColor(), font=labelFont, borderwidth=2, relief="groove")


playerCardP1_1.grid(row = 0, column = 0, padx = 25)
playerCardP1_2.grid(row = 0, column = 1, padx = 0)

cardFrameP1.grid(row=0, columnspan = 8, sticky=W + E)

playerLabelP1.grid(row=1, column = 0)
playerNameP1.grid(row=1, column=1, columnspan=2)
playerChipsP1.grid(row=1, column=3)
playerBetP1.grid(row=1, column = 5, columnspan=3)
emptyLabelP1.grid(row=1, column=4)

setNameBtnP1.grid(row=2, column=1)
getChipsButtonP1.grid(row=2, column= 3)
betButtonP1.grid(row=2, column=5)
allInButtonP1.grid(row=2, column=6)
foldButtonP1.grid(row=2, column=7)
emptyLabelP1.grid(row=2, column=4)

playerFrameP2 = Frame(mainGame, width=200, height=100, borderwidth=2)

strVarP2 = StringVar()

playerLabelP2 = Label(playerFrameP2, text="Name")
playerNameP2 = Entry(playerFrameP2)
cardFrameP2 = Frame(playerFrameP2, bg="green")
setNameBtnP2 = Button(playerFrameP2, text="Join", command= lambda: createPlayer(playerNameP2, setNameBtnP2, playerChipsP2, playerNameP2.get(),playerBetP2, betButtonP2, allInButtonP2, foldButtonP2, getChipsButtonP2))
playerChipsP2 = Label(playerFrameP2, text="Chips: ")
getChipsButtonP2 = Button(playerFrameP2, text="Get Chips", command= lambda: givePlayerChips(playerChipsP2, playerNameP2.get()), state=DISABLED)
playerBetP2 = Entry(playerFrameP2, state=DISABLED, textvariable=strVarP2)
betButtonP2 = Button(playerFrameP2, text="Bet", state=DISABLED, command= lambda: btnBet(playerChipsP2,playerBetP2,playerNameP2))
allInButtonP2 = Button(playerFrameP2, text="All In", state=DISABLED, command= lambda: btnAllIn(playerChipsP2, playerBetP2, playerNameP2, betButtonP2, allInButtonP2, foldButtonP2, strVarP2))
foldButtonP2 = Button(playerFrameP2, text="Fold", state=DISABLED, command=lambda: btnFold(playerBetP2,playerNameP2, betButtonP2, allInButtonP2, foldButtonP2))

emptyLabelP2 = Label(playerFrameP2, text ="    ")

playerCardP2_1 = Label(cardFrameP2, padx=10, pady=15, bg="White", text=newCard, fg=newCard.getCardColor(), font=labelFont, borderwidth=2, relief="groove")

playerCardP2_2 = Label(cardFrameP2, padx=10, pady=15, bg="White", text=newCard, fg=newCard.getCardColor(), font=labelFont, borderwidth=2, relief="groove")


playerCardP2_1.grid(row = 0, column = 0, padx = 25)
playerCardP2_2.grid(row = 0, column = 1, padx = 0)

cardFrameP2.grid(row=0, columnspan = 8, sticky=W + E)

playerLabelP2.grid(row=1, column = 0)
playerNameP2.grid(row=1, column=1, columnspan=2)
playerChipsP2.grid(row=1, column=3)
playerBetP2.grid(row=1, column = 5, columnspan=3)
emptyLabelP2.grid(row=1, column=4)

setNameBtnP2.grid(row=2, column=1)
getChipsButtonP2.grid(row=2, column= 3)
betButtonP2.grid(row=2, column=5)
allInButtonP2.grid(row=2, column=6)
foldButtonP2.grid(row=2, column=7)
emptyLabelP2.grid(row=2, column=4)

playerFrameP3 = Frame(mainGame, width=200, height=100, borderwidth=2)

strVarP3 = StringVar()

playerLabelP3 = Label(playerFrameP3, text="Name")
playerNameP3 = Entry(playerFrameP3)
cardFrameP3 = Frame(playerFrameP3, bg="green")
setNameBtnP3 = Button(playerFrameP3, text="Join", command= lambda: createPlayer(playerNameP3, setNameBtnP3, playerChipsP3, playerNameP3.get(),playerBetP3, betButtonP3, allInButtonP3, foldButtonP3, getChipsButtonP3))
playerChipsP3 = Label(playerFrameP3, text="Chips: ")
getChipsButtonP3 = Button(playerFrameP3, text="Get Chips", command= lambda: givePlayerChips(playerChipsP3, playerNameP3.get()), state=DISABLED)
playerBetP3 = Entry(playerFrameP3, state=DISABLED, textvariable=strVarP3)
betButtonP3 = Button(playerFrameP3, text="Bet", state=DISABLED, command= lambda: btnBet(playerChipsP3,playerBetP3,playerNameP3))
allInButtonP3 = Button(playerFrameP3, text="All In", state=DISABLED, command= lambda: btnAllIn(playerChipsP3, playerBetP3, playerNameP3, betButtonP3, allInButtonP3, foldButtonP3, strVarP3))
foldButtonP3 = Button(playerFrameP3, text="Fold", state=DISABLED, command=lambda: btnFold(playerBetP3,playerNameP3, betButtonP3, allInButtonP3, foldButtonP3))

emptyLabelP3 = Label(playerFrameP3, text ="    ")

playerCardP3_1 = Label(cardFrameP3, padx=10, pady=15, bg="White", text=newCard, fg=newCard.getCardColor(), font=labelFont, borderwidth=2, relief="groove")

playerCardP3_2 = Label(cardFrameP3, padx=10, pady=15, bg="White", text=newCard, fg=newCard.getCardColor(), font=labelFont, borderwidth=2, relief="groove")


playerCardP3_1.grid(row = 0, column = 0, padx = 25)
playerCardP3_2.grid(row = 0, column = 1, padx = 0)

cardFrameP3.grid(row=0, columnspan = 8, sticky=W + E)

playerLabelP3.grid(row=1, column = 0)
playerNameP3.grid(row=1, column=1, columnspan=2)
playerChipsP3.grid(row=1, column=3)
playerBetP3.grid(row=1, column = 5, columnspan=3)
emptyLabelP3.grid(row=1, column=4)

setNameBtnP3.grid(row=2, column=1)
getChipsButtonP3.grid(row=2, column= 3)
betButtonP3.grid(row=2, column=5)
allInButtonP3.grid(row=2, column=6)
foldButtonP3.grid(row=2, column=7)
emptyLabelP3.grid(row=2, column=4)

playerFrameP4 = Frame(mainGame, width=200, height=100, borderwidth=2)

strVarP4 = StringVar()

playerLabelP4 = Label(playerFrameP4, text="Name")
playerNameP4 = Entry(playerFrameP4)
cardFrameP4 = Frame(playerFrameP4, bg="green")
setNameBtnP4 = Button(playerFrameP4, text="Join", command= lambda: createPlayer(playerNameP4, setNameBtnP4, playerChipsP4, playerNameP4.get(),playerBetP4, betButtonP4, allInButtonP4, foldButtonP4, getChipsButtonP4))
playerChipsP4 = Label(playerFrameP4, text="Chips: ")
getChipsButtonP4 = Button(playerFrameP4, text="Get Chips", command= lambda: givePlayerChips(playerChipsP4, playerNameP4.get()), state=DISABLED)
playerBetP4 = Entry(playerFrameP4, state=DISABLED, textvariable=strVarP4)
betButtonP4 = Button(playerFrameP4, text="Bet", state=DISABLED, command= lambda: btnBet(playerChipsP4,playerBetP4,playerNameP4))
allInButtonP4 = Button(playerFrameP4, text="All In", state=DISABLED, command= lambda: btnAllIn(playerChipsP4, playerBetP4, playerNameP4, betButtonP4, allInButtonP4, foldButtonP4, strVarP4))
foldButtonP4 = Button(playerFrameP4, text="Fold", state=DISABLED, command=lambda: btnFold(playerBetP4,playerNameP4, betButtonP4, allInButtonP4, foldButtonP4))

emptyLabelP4 = Label(playerFrameP4, text ="    ")

playerCardP4_1 = Label(cardFrameP4, padx=10, pady=15, bg="White", text=newCard, fg=newCard.getCardColor(), font=labelFont, borderwidth=2, relief="groove")

playerCardP4_2 = Label(cardFrameP4, padx=10, pady=15, bg="White", text=newCard, fg=newCard.getCardColor(), font=labelFont, borderwidth=2, relief="groove")


playerCardP4_1.grid(row = 0, column = 0, padx = 25)
playerCardP4_2.grid(row = 0, column = 1, padx = 0)

cardFrameP4.grid(row=0, columnspan = 8, sticky=W + E)

playerLabelP4.grid(row=1, column = 0)
playerNameP4.grid(row=1, column=1, columnspan=2)
playerChipsP4.grid(row=1, column=3)
playerBetP4.grid(row=1, column = 5, columnspan=3)
emptyLabelP4.grid(row=1, column=4)

setNameBtnP4.grid(row=2, column=1)
getChipsButtonP4.grid(row=2, column= 3)
betButtonP4.grid(row=2, column=5)
allInButtonP4.grid(row=2, column=6)
foldButtonP4.grid(row=2, column=7)
emptyLabelP4.grid(row=2, column=4)

tableChipsStr = StringVar()
tableChipsStr.set("Chips: " + str(gameTable.getChipPile()))
tableChipsLabel = Label(mainGame, textvariable=tableChipsStr)

dealerStr = StringVar()
dealerStr.set("Dealer: " + gameTable.getDealerPlayer())
dealerLabel = Label(mainGame, textvariable=dealerStr)

playerFrameP1.grid(row=0, column=0, padx = 5, pady=5)
playerFrameP2.grid(row=1, column=0, padx = 5, pady=5)
playerFrameP3.grid(row=2, column=0 ,padx = 5, pady=5)
playerFrameP4.grid(row=3, column=0, padx = 5, pady=5)

tableChipsLabel.grid(row=2, columns=9, padx= (450,30), pady=5)
dealerLabel.grid(row=2, columns=10, padx= (600,30), pady=5)

multiPlayerFrame.grid(row=3, columnspan=2)

gameFrame.pack(side=LEFT, fill=Y)

playerFrame1 = Frame(mainGame, width=200, height=100)

#playerFrame1.grid(column=0, row=2)

mainGame.pack(side=LEFT, expand=True)

mainThread = th.Thread(target=mainloop())

mainThread.start()
