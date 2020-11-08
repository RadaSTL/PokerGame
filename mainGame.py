from tkinter import *
from tkinter.font import *
import socket
import subprocess
import threading as th

root = Tk()
root.title("Poker Game")

gameFrame = Frame (root, height = 400, width = 300)

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

multiPlayerFrame.grid(row=3, columnspan=2)



gameFrame.pack()



'''
playerBox = Frame(root)

playerFrame = Frame(playerBox, width=100, height=50)
betButton = Button(playerFrame,text="Bet")
allInButton = Button(playerFrame,text="All In")
foldButton = Button(playerFrame,text="Fold")
betEntry = Entry(playerFrame)

betEntry.grid(row=0,columnspan=3)
betButton.grid(row=1,column=0)
allInButton.grid(row=1,column=1)
foldButton.grid(row=1,column=2)

labelFont = Font(size = 20)

playerCardFrame = Frame(playerBox, bg="green")

newCard = c.Card(2,14)

card = Label(playerCardFrame, padx=10, pady=15, bg="White", text=newCard, fg=newCard.getCardColor(), font=labelFont,  borderwidth=2, relief="groove")

newCard = c.Card(2,4)

card1 = Label(playerCardFrame, padx=10, pady=15, bg="White", text=newCard, fg=newCard.getCardColor(), font=labelFont,  borderwidth=2, relief="groove")


card.grid(row = 0, column = 0, padx=5, pady=5)
card1.grid(row = 0, column = 1, padx=5, pady=5)

playerFrame['width'] = playerCardFrame['width']
playerCardFrame.pack()
playerFrame.pack()
playerBox.pack()

'''

mainThread = th.Thread(target=mainloop())

mainThread.start()

def callSubprocess():
    subprocess.call(['python', 'EndPoint.py'])

th1 = th.Thread(target = callSubprocess())