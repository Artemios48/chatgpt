from tkinter import *
import random
from tkinter import messagebox as mb

class Interface:
    def __init__(self, window):
        self.score = 0
        self.record = 0
        self.window = window
        self.titleLb = Label(text="2048", font="Arial 82 bold")
        self.titleLb.place(x=5, y=5)

        self.restartLb = Label(text="НАЧАТЬ СНАЧАЛА",
                               font="Arial 18 bold",
                               fg="#f65e3b")
        self.restartLb.place(x=5, y=120)

        self.scoreLb = Label(text="СЧЁТ: 0\nРЕКОРД:0",font="Arial 16", justify=LEFT)
        self.scoreLb.place(x=270, y=25)

        self.colors = {0:"#cdc1b4",
                       2:"#eee4da",
                       4:"#ede0c8",
                       8:"#f2b179",
                       16:"#f59563",
                       32:"#f67c5f",
                       64:"#f65e3b",
                       128:"#edcf72",
                       256:"#edcc61",
                       512:"#edc850",
                       1024:"#edc53f",
                       2048:"#edc22e"}
        self.map = [[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]]
        self.emptyMap = []
        self.tiles = []

        for i in range(4):
            line = []
            for j in range(4):
                line.append(Button(text="2048",
                                   width=5,
                                   font="Arial 25 bold",
                                   height=2,
                                   state=DISABLED))
                line[j].place(x=j*110+5,
                              y=i*105+200)
            self.tiles.append(line)
        self.newGame()
        self.window.bind("<a>", self.leftMove)
        self.window.bind("<d>", self.rightMove)
        self.window.bind("<w>", self.upMove)
        self.window.bind("<s>", self.downMove)
        self.restartLb.bind("<Button-1>",self.restartLbClick)
        self.window.protocol("WM_DELETE_WINDOW", self.onClose)

    def onClose(self):
        f = open("record.txt", "w")
        f.write(str(self.record))
        f.close()
        self.window.destroy()

    def restartLbClick(self, event):
        self.newGame()

    def newGame(self):
        try:
            f = open("record.txt", "r")
            r = int(f.readline())
            if r > self.record:
                self.record = r
            f.close()
        except:
            self.record = 0
        self.map = [[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0]]
        self.score = 0
        self.updateEmptyMap()
        self.addTile()
        self.addTile()
        self.updateTiles()

    def leftMove(self,event):
        self.move("left")
    def rightMove(self,event):
        self.move("right")
    def upMove(self,event):
        self.move("up")
    def downMove(self,event):
        self.move("down")

    def move(self,direction):
        if self.checkLose() != False:
            return
        oldMap = str(self.map)
        if direction == "left":
            for i in range (4):
                self.map[i] = self.moveLine(list(self.map[i]))
        elif direction == 'right':
            for i in range(4):
                self.map[i].reverse()
                self.map[i] = self.moveLine(list(self.map[i]))
                self.map[i].reverse()
        elif direction == 'up':
            for j in range(4):
                line = []
                for i in range(4):
                    line.append(self.map[i][j])
                line = self.moveLine(line)
                for i in range(4):
                    self.map[i][j] = line[i]
        elif direction == 'down':
            for j in range(4):
                line = []
                for i in range(4):
                    line.append(self.map[i][j])
                line.reverse()
                line = self.moveLine(line)
                line.reverse()
                for i in range(4):
                    self.map[i][j] = line[i]
        self.updateEmptyMap()
        if oldMap != str(self.map):
            self.addTile()
        self.updateTiles()

    def moveLine(self,line):
        while 0 in line:
            line.remove(0)
        for i in range(len(line)-1):
            if line[i] == line[i+1]:
                line[i]*=2
                self.score +=line[i]
                line[i+1] = 0
        while 0 in line:
            line.remove(0)
        while len(line) < 4:
            line.append(0)
        return line
    def checkLose(self):
        if len(self.emptyMap) != 0:
            return False
        for i in range(4):
            for j in range(3):
                if self.map[i][j] == self.map[i][j+1]:
                    return False
        for j in range(4):
            for i in range(3):
                if self.map[i][j] == self.map[i+1][j]:
                    return False
        answer = mb.askyesno('Увы', 'Вы проиграли! Начнём сначала?')
        if answer == True:
            self.newGame()
            return
        else:
            self.onClose()
            return
    def updateEmptyMap(self):
        self.emptyMap.clear()
        for i in range(4):
            for j in range(4):
                if self.map[i][j] == 0:
                    self.emptyMap.append([i,j])

    def addTile(self):
        if len(self.emptyMap) == 0:
            return
        t = random.choice(self.emptyMap)
        newTile = random.choice([2,2,2,2,2,2,2,2,2,4])
        self.map[t[0]][t[1]] = newTile
        self.updateEmptyMap()
    def updateTiles(self):
        for i in range(4):
            for j in range(4):
                if self.map[i][j] != 0:
                    self.tiles[i][j].configure(text = self.map[i][j])
                else:
                    self.tiles[i][j].configure(text='')
                if self.map[i][j]<2048:
                    color = self.colors[self.map[i][j]]
                else:
                    color = self.colors[2048]
                self.tiles[i][j].configure(bg = color,disabledforeground = 'black')
            if self.score > self.record:
                self.record = self.score
            self.scoreLb.configure(text=f'СЧЁТ:{self.score}\nРЕКОРД:{self.record}')



