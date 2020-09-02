from colors import Color
from os import system
from time import sleep

color = Color()

class Game():
    figures = {
        0: {"p": "B", "f": "T"},
        1: {"p": "B", "f": "S"},
        2: {"p": "B", "f": "L"},
        3: {"p": "B", "f": "D"},
        4: {"p": "B", "f": "K"},
        5: {"p": "B", "f": "L"},
        6: {"p": "B", "f": "S"},
        7: {"p": "B", "f": "T"},
        8: {"p": "B", "f": "B"},
        9: {"p": "B", "f": "B"},
        10: {"p": "B", "f": "B"},
        11: {"p": "B", "f": "B"},
        12: {"p": "B", "f": "B"},
        13: {"p": "B", "f": "B"},
        14: {"p": "B", "f": "B"},
        15: {"p": "B", "f": "B"},
        48: {"p": "W", "f": "B"},
        49: {"p": "W", "f": "B"},
        50: {"p": "W", "f": "B"},
        51: {"p": "W", "f": "B"},
        52: {"p": "W", "f": "B"},
        53: {"p": "W", "f": "B"},
        54: {"p": "W", "f": "B"},
        55: {"p": "W", "f": "B"},
        56: {"p": "W", "f": "T"},
        57: {"p": "W", "f": "S"},
        58: {"p": "W", "f": "L"},
        59: {"p": "W", "f": "D"},
        60: {"p": "W", "f": "K"},
        61: {"p": "W", "f": "L"},
        62: {"p": "W", "f": "S"},
        63: {"p": "W", "f": "T"}
    }
    win = False
    colorToFieldList = {}
    moves = {}
    gameTurns = []
    countTurns = 0
    playerKey = ""
    actualPlayer = ""
    revert = False
    lose = False
    isRochade = False
    allWhiteNormalTurns = []
    allBlackNormalTurns = []
    allWhiteDestroyTurns = []
    allBlackDestroyTurns = []

    def wayToMoveFigures(self, start, ziel):
        moves = {}
        fromStartLeft = start % 8
        fromZielLeft = ziel % 8
        fromStartTop = int(start / 8)
        fromZielTop = int(ziel / 8)
        top = 0
        bottom = 0
        left = 0
        right = 0
        if (fromStartTop > fromZielTop):
            top = fromStartTop - fromZielTop
        else:
            bottom = fromZielTop - fromStartTop
        if(fromZielLeft > fromStartLeft):
            right = fromZielLeft - fromStartLeft
        else:
            left = fromStartLeft - fromZielLeft

        if(top > 0):
            i = 0
            while i <= top:
                pos = start - (i * 8)
                if (len(moves) == 0 or moves[len(moves) - 1] != pos):
                    moves.update({len(moves):pos})
                data = {pos: "red"}
                self.colorToFieldList.update(data)
                i = i + 1

            if(left > 0):
                i = 0
                while i <= left:
                    pos = start - top * 8 - i
                    if (len(moves) == 0 or moves[len(moves) - 1] != pos):
                        moves.update({len(moves):pos})
                    data = {pos: "red"}
                    self.colorToFieldList.update(data)
                    i = i + 1

            if (right > 0):
                i = 0
                while i <= right:
                    pos = start - top * 8 + i
                    if (len(moves) == 0 or moves[len(moves) - 1] != pos):
                        moves.update({len(moves):pos})
                    data = {pos: "red"}
                    self.colorToFieldList.update(data)
                    i = i + 1

        if (bottom > 0):
            i = 0
            while i <= bottom:
                pos = start + (i * 8)
                if (len(moves) == 0 or moves[len(moves) - 1] != pos):
                    moves.update({len(moves):pos})
                data = {pos: "red"}
                self.colorToFieldList.update(data)
                i = i + 1

            if (left > 0):
                i = 0
                while i <= left:
                    pos = start + bottom * 8 - i
                    if (len(moves) == 0 or moves[len(moves) - 1] != pos):
                        moves.update({len(moves):pos})
                    data = {pos: "red"}
                    self.colorToFieldList.update(data)
                    i = i + 1

            if (right > 0):
                i = 0
                while i <= right:
                    pos = start + bottom * 8 + i
                    if (len(moves) == 0 or moves[len(moves) - 1] != pos):
                        moves.update({len(moves):pos})
                    data = {pos: "red"}
                    self.colorToFieldList.update(data)
                    i = i + 1

        self.moves.update({len(self.moves): moves})

        print(self.moves)

        self.completeField()
        self.colorToFieldList = {}
        self.moves = {}
        return True

    def setWinToPlayer(self, player):
        self.win = player

    def __init__(self):
        self.clear()
        print(color.greenColor("Welcome!"))
        print()
        print("This is a python chess game, it works on a Raspberry Pi 3 Model B and Arduiono UNO.")
        print("The game show you turns on a real chess field.")
        print("It means, you made you turns here and the Script shows you turns on the field.")
        print()
        print("Please press enter to start.")
        input()
        self.clear()

        print("Alright! Lets get started..")
        print(color.greenColor("Good Luck!"))

        self.gameplay()

        self.clear()

        print("The game is over!")
        print(color.greenColor(self.win), color.greenColor("has won!"))
        print()
        self.completeField()
        print()
        print("All turns:")
        i = 0
        while i < len(self.gameTurns):
            print(i + 1, "| Start position:", self.fieldPositionToFieldName(self.gameTurns[i]), "| End position:", self.fieldPositionToFieldName(self.gameTurns[i + 1]))
            i = i + 2

    def fieldPositionToFieldName(self, pos):
        X = 8 - int(pos / 8)
        Y = pos % 8
        if(Y == 0):
            name = "A"
        elif(Y == 1):
            name = "B"
        elif(Y == 2):
            name = "C"
        elif(Y == 3):
            name = "D"
        elif(Y == 4):
            name = "E"
        elif(Y == 5):
            name = "F"
        elif(Y == 6):
            name = "G"
        elif(Y == 7):
            name = "H"

        name += str(X)
        return name

    def setAllTurns(self):
        self.allBlackDestroyTurns = []
        self.allWhiteDestroyTurns = []
        self.allBlackNormalTurns = []
        self.allWhiteNormalTurns = []
        i = 0
        while i < 64:
            if(i in self.figures.keys()):
                figure = self.getFigureOnField(i)
                turns = self.getTurnsForFigureOnField(i)
                if(figure["p"] == "B") :
                    j = 0
                    while j < len(turns[0]):
                        self.allBlackNormalTurns.append(turns[0][j])
                        j = j + 1
                    j = 0
                    while j < len(turns[1]):
                        self.allBlackDestroyTurns.append(turns[1][j])
                        j = j + 1
                else:
                    j = 0
                    while j < len(turns[0]):
                        self.allWhiteNormalTurns.append(turns[0][j])
                        j = j + 1
                    j = 0
                    while j < len(turns[1]):
                        self.allWhiteDestroyTurns.append(turns[1][j])
                        j = j + 1
            i = i + 1
        return True

    def getFigureOnField(self, field):
        if(field in self.figures.keys()):
            return self.figures[field]
        return False

    def getTurnsForFigureOnField(self, field):
        figure = self.getFigureOnField(field)
        if(figure["f"] == "T"):
            turns = self.turmTurns(field)
        elif(figure["f"] == "L"):
            turns = self.laeuferTurns(field)
        elif(figure["f"] == "K"):
            turns = self.koenigTurns(field)
        elif(figure["f"] == "D"):
            turns = self.damenTurns(field)
        elif(figure["f"] == "S"):
            turns = self.springerTurns(field)
        elif(figure["f"] == "B"):
            turns = self.bauernTurns(field)
        else:
            turns = []
            turns.append([])
            turns.append([])
        return turns

    def gameplay(self):
        while(self.win == False):
            self.revert = True
            while self.revert == True:
                self.revert = False
                self.isRochade = False
                if (self.countTurns != 0) :
                    self.clear()
                if(self.countTurns % 2 == 0):
                    self.actualPlayer = "White"
                    self.playerKey = "W"
                else:
                    self.actualPlayer = "Black"
                    self.playerKey = "B"

                print("Player is", self.actualPlayer)

                self.setAllTurns()

                schach = self.myChessControll()

                self.completeField()

                if (schach == True):
                    print(color.redColor("You're in chess!"))

                startField = False
                while (startField is False and self.lose is False):
                    print(color.yellowColor("Input start position:"))
                    raw_input = input()
                    if (len(raw_input) > 0 and raw_input[0] == "/") :
                        if(self.commandList(raw_input) is False):
                            print(color.redColor("Command not found!"))
                    elif(len(raw_input) > 0):
                        rawStartField = self.isValidInput(raw_input)
                        if(rawStartField is not False):
                            startField = self.isOnPositionFigureOfMyTeam(rawStartField)
                    else:
                        print(color.redColor("Invalid input!"))
                endFields = self.getTurnsForFigureOnField(startField)
                endField = False
                while (endField is False and self.lose is False):
                    print(color.yellowColor("Input end position:"))
                    raw_input = input()
                    if (len(raw_input) > 0 and raw_input[0] == "/") :
                        self.commandList(raw_input)
                        if(self.revert == True):
                            endField = True
                    elif(len(raw_input) > 0):
                        rawEndField = self.isValidInput(raw_input)
                        if(rawEndField is not False):
                            if(rawEndField in endFields[0] or rawEndField in endFields[1]):
                                if(self.simulateIsChessAfterTurn(startField, rawEndField, 1) == False):
                                    endField = rawEndField
                                    self.setIfIsRochade(startField, endField)
                                else:
                                    print(color.redColor("It's not allow to stay in chess position after turn!"))
                            else:
                                print(color.redColor("Move not possible!"))
                    else:
                        print(color.redColor("Invalid input!"))
            if (self.lose is False):
                if(self.isRochade is False):
                    self.wayToMoveFigures(startField, endField)
                    self.updateFigureOnField(startField, endField)
                else:
                    self.updateFigureOnField(startField, endField)
                    if(self.isRochade > endField):
                        self.updateFigureOnField(self.isRochade, endField - 1)
                    else:
                        self.updateFigureOnField(self.isRochade, endField + 1)
                self.gameTurns.append(startField)
                self.gameTurns.append(endField)
                self.countTurns = self.countTurns + 1

                self.setAllTurns()
                if (self.ifCheckMated() == True):
                    self.win = self.actualPlayer
            else:
                if(self.playerKey == "B"):
                    self.win = "White"
                else:
                    self.win = "Black"

    def setIfIsRochade(self, start, ziel):
        if(self.figures[start]["f"] == "K"):
            if(start + 2 == ziel):
                self.isRochade = start + 3
                return True
            if(start - 2 == ziel):
                self.isRochade = start - 4
            return False
        return False

    def completeField(self):
        print(color.cyanBackground("  ") + color.cyanBackground("A ") + color.cyanBackground("B ") + color.cyanBackground("C ") + color.cyanBackground("D ") + color.cyanBackground("E ") + color.cyanBackground("F ") + color.cyanBackground("G ") + color.cyanBackground("H ") + color.cyanBackground("  "))
        print(color.cyanBackground("8 ") + self.field(0) + self.field(1) + self.field(2) + self.field(3) + self.field(4) + self.field(5) + self.field(6) + self.field(7) + color.cyanBackground(" 8"))
        print(color.cyanBackground("7 ") + self.field(8) + self.field(9) + self.field(10) + self.field(11) + self.field(12) + self.field(13) + self.field(14) + self.field(15) + color.cyanBackground(" 7"))
        print(color.cyanBackground("6 ") + self.field(16) + self.field(17) + self.field(18) + self.field(19) + self.field(20) + self.field(21) + self.field(22) + self.field(23) + color.cyanBackground(" 6"))
        print(color.cyanBackground("5 ") + self.field(24) + self.field(25) + self.field(26) + self.field(27) + self.field(28) + self.field(29) + self.field(30) + self.field(31) + color.cyanBackground(" 5"))
        print(color.cyanBackground("4 ") + self.field(32) + self.field(33) + self.field(34) + self.field(35) + self.field(36) + self.field(37) + self.field(38) + self.field(39) + color.cyanBackground(" 4"))
        print(color.cyanBackground("3 ") + self.field(40) + self.field(41) + self.field(42) + self.field(43) + self.field(44) + self.field(45) + self.field(46) + self.field(47) + color.cyanBackground(" 3"))
        print(color.cyanBackground("2 ") + self.field(48) + self.field(49) + self.field(50) + self.field(51) + self.field(52) + self.field(53) + self.field(54) + self.field(55) + color.cyanBackground(" 2"))
        print(color.cyanBackground("1 ") + self.field(56) + self.field(57) + self.field(58) + self.field(59) + self.field(60) + self.field(61) + self.field(62) + self.field(63) + color.cyanBackground(" 1"))
        print(color.cyanBackground("  ") + color.cyanBackground("A ") + color.cyanBackground("B ") + color.cyanBackground("C ") + color.cyanBackground("D ") + color.cyanBackground("E ") + color.cyanBackground("F ") + color.cyanBackground("G ") + color.cyanBackground("H ") + color.cyanBackground("  "))

    def chessControll(self):
        i = 0
        while(i < 64):
            if (i in self.figures.keys()):
                if (self.figures[i]["p"] != self.playerKey and self.figures[i]["f"] == "K"):
                    if (self.playerKey != "W"):
                        if (i in self.allBlackDestroyTurns):
                            return True
                        else:
                            return False
                    else:
                        if (i in self.allWhiteDestroyTurns):
                            return True
                        else:
                            return False
            i = i + 1
        return False

    def myChessControll(self):
        i = 0
        while(i < 64):
            if (i in self.figures.keys()):
                if (self.figures[i]["p"] == self.playerKey and self.figures[i]["f"] == "K"):
                    if (self.playerKey == "W"):
                        if (i in self.allBlackDestroyTurns):
                            return True
                        else:
                            return False
                    else:
                        if (i in self.allWhiteDestroyTurns):
                            return True
                        else:
                            return False
            i = i + 1
        return False

    def ifCheckMated(self):
        i = 0
        while i < 64:
            if(i in self.figures.keys()):
                if (self.figures[i]["p"] != self.playerKey and self.figures[i]["f"] == "K"):
                    if (self.playerKey == "B"):
                        if (i in self.allBlackDestroyTurns):
                            escapeMoves = self.getTurnsForFigureOnField(i)
                            j = 0
                            while j < len(escapeMoves[0]):
                                if (escapeMoves[0][j] not in self.allBlackNormalTurns and escapeMoves[0][j] not in self.allBlackDestroyTurns):
                                    if(self.simulateIsChessAfterTurn(i, escapeMoves[0][j], 2) is False):
                                        return False
                                j = j + 1
                            j = 0
                            while j < len(escapeMoves[1]):
                                if(escapeMoves[1][j] not in self.allBlackNormalTurns and escapeMoves[1][j] not in self.allBlackDestroyTurns):
                                    if (self.simulateIsChessAfterTurn(i, escapeMoves[1][j], 2) is False):
                                        return False
                                j = j + 1

                            k = 0
                            anzFiguren = 0
                            capture = []
                            while k < 64:
                                if(k in self.figures.keys()):
                                    if(self.figures[k]["p"] == self.playerKey):
                                        turns = self.getTurnsForFigureOnField(k)
                                        if(i in turns[0] or i in turns[1]):
                                            anzFiguren = anzFiguren + 1
                                            capture.append(k)
                                k = k + 1

                            if(anzFiguren == 1):
                                figure = self.getFigureOnField(capture[0])
                                if(figure["f"] == "L"):
                                    if(capture[0] <= i):
                                        if((i - capture[0]) % 9 == 0):
                                            l = capture[0] + 9
                                            while(l < i):
                                                capture.append(l)
                                                l = l + 9
                                        elif((i - capture[0]) % 7 == 0):
                                            l = capture[0] + 7
                                            while (l < i):
                                                capture.append(l)
                                                l = l + 7
                                    else:
                                        if((capture[0] - i) % 9  == 0):
                                            l = capture[0] - 9
                                            while (l > i):
                                                capture.append(l)
                                                l = l - 9
                                        elif((capture[0] - i) % 7 == 0):
                                            l = capture[0] - 7
                                            while (l > i):
                                                capture.append(l)
                                                l = l - 7
                                elif(figure["f"] == "T"):
                                    if(capture[0] < i):
                                        if((i - capture[0]) % 8 == 0):
                                            l = capture[0] + 8
                                            while l < i:
                                                capture.append(l)
                                                l = l + 8
                                        else:
                                            l = capture[0] + 1
                                            while l < i:
                                                capture.append(l)
                                                l = l + 1
                                    else:
                                        if((capture[0] - i) % 8 == 0):
                                            l = capture[0] - 8
                                            while l > i:
                                                capture.append(l)
                                                l = l - 8
                                        else:
                                            l = capture[0] - 1
                                            while l > i:
                                                capture.append(l)
                                                l = l - 1
                                elif(figure["f"] == "D"):
                                    if (capture[0] <= i):
                                        if ((i - capture[0]) % 9 == 0):
                                            l = capture[0] + 9
                                            while (l < i):
                                                capture.append(l)
                                                l = l + 9
                                        elif ((i - capture[0]) % 7 == 0):
                                            l = capture[0] + 7
                                            while (l < i):
                                                capture.append(l)
                                                l = l + 7
                                        elif((i - capture[0]) % 8 == 0):
                                            l = capture[0] + 8
                                            while l < i:
                                                capture.append(l)
                                                l = l + 8
                                        else:
                                            l = capture[0] + 1
                                            while l < i:
                                                capture.append(l)
                                                l = l + 1
                                    else:
                                        if ((capture[0] - i) % 9 == 0):
                                            l = capture[0] - 9
                                            while (l > i):
                                                capture.append(l)
                                                l = l - 9
                                        elif ((capture[0] - i) % 7 == 0):
                                            l = capture[0] - 7
                                            while (l > i):
                                                capture.append(l)
                                                l = l - 7
                                        elif((capture[0] - i) % 8 == 0):
                                            l = capture[0] - 8
                                            while l > i:
                                                capture.append(l)
                                                l = l - 8
                                        else:
                                            l = capture[0] - 1
                                            while l > i:
                                                capture.append(l)
                                                l = l - 1

                                m = 0
                                while m < 64:
                                    if (m in self.figures.keys() and self.figures[m]["p"] == "W"):
                                        turns = self.getTurnsForFigureOnField(m)
                                        if (self.figures[m]["f"] == "K"):
                                            if (capture[0] in turns[1]):
                                                if (self.simulateIsChessAfterTurn(m, capture[0], 2) == False):
                                                    return False
                                        else:
                                            n = 0
                                            while n < len(capture):
                                                if (capture[n] in turns[0] or capture[n] in turns[1]):
                                                    if (self.simulateIsChessAfterTurn(m, capture[n], 2) == False):
                                                        return False
                                                n = n + 1
                                    m = m + 1
                                return True
                            else:
                                return True
                        else:
                            return False
                    else:
                        if (i in self.allWhiteDestroyTurns):
                            escapeMoves = self.getTurnsForFigureOnField(i)
                            j = 0
                            while j < len(escapeMoves[0]):
                                if (escapeMoves[0][j] not in self.allWhiteNormalTurns and escapeMoves[0][j] not in self.allWhiteDestroyTurns):
                                    if (self.simulateIsChessAfterTurn(i, escapeMoves[0][j], 2) is False):
                                        return False
                                j = j + 1
                            j = 0
                            while j < len(escapeMoves[1]):
                                if(self.simulateIsChessAfterTurn(i, escapeMoves[1][j], 2) == False):
                                    if (self.simulateIsChessAfterTurn(i, escapeMoves[1][j], 2) is False):
                                        return False
                                j = j + 1

                            # Finde Figuren die den König an der aktuellen stelle schlagen können
                            k = 0
                            anzFiguren = 0
                            capture = []
                            while k < 64:
                                if (k in self.figures.keys()):
                                    if (self.figures[k]["p"] == self.playerKey):
                                        turns = self.getTurnsForFigureOnField(k)
                                        if (i in turns[0] or i in turns[1]):
                                            anzFiguren = anzFiguren + 1
                                            capture.append(k)
                                k = k + 1

                            if (anzFiguren == 1):
                                figure = self.getFigureOnField(capture[0])
                                if (figure["f"] == "L"):
                                    if (capture[0] <= i):
                                        if ((i - capture[0]) % 9 == 0):
                                            l = capture[0] + 9
                                            while (l < i):
                                                capture.append(l)
                                                l = l + 9
                                        elif ((i - capture[0]) % 7 == 0):
                                            l = capture[0] + 7
                                            while (l < i):
                                                capture.append(l)
                                                l = l + 7
                                    else:
                                        if ((capture[0] - i) % 9 == 0):
                                            l = capture[0] - 9
                                            while (l > i):
                                                capture.append(l)
                                                l = l - 9
                                        elif ((capture[0] - i) % 7 == 0):
                                            l = capture[0] - 7
                                            while (l > i):
                                                capture.append(l)
                                                l = l - 7
                                elif (figure["f"] == "T"):
                                    if (capture[0] < i):
                                        if ((i - capture[0]) % 8 == 0):
                                            l = capture[0] + 8
                                            while l < i:
                                                capture.append(l)
                                                l = l + 8
                                        else:
                                            l = capture[0] + 1
                                            while l < i:
                                                capture.append(l)
                                                l = l + 1
                                    else:
                                        if ((capture[0] - i) % 8 == 0):
                                            l = capture[0] - 8
                                            while l > i:
                                                capture.append(l)
                                                l = l - 8
                                        else:
                                            l = capture[0] - 1
                                            while l > i:
                                                capture.append(l)
                                                l = l - 1
                                elif (figure["f"] == "D"):
                                    if (capture[0] <= i):
                                        if ((i - capture[0]) % 9 == 0):
                                            l = capture[0] + 9
                                            while (l < i):
                                                capture.append(l)
                                                l = l + 9
                                        elif ((i - capture[0]) % 7 == 0):
                                            l = capture[0] + 7
                                            while (l < i):
                                                capture.append(l)
                                                l = l + 7
                                        elif ((i - capture[0]) % 8 == 0):
                                            l = capture[0] + 8
                                            while l < i:
                                                capture.append(l)
                                                l = l + 8
                                        else:
                                            l = capture[0] + 1
                                            while l < i:
                                                capture.append(l)
                                                l = l + 1
                                    else:
                                        if ((capture[0] - i) % 9 == 0):
                                            l = capture[0] - 9
                                            while (l > i):
                                                capture.append(l)
                                                l = l - 9
                                        elif ((capture[0] - i) % 7 == 0):
                                            l = capture[0] - 7
                                            while (l > i):
                                                capture.append(l)
                                                l = l - 7
                                        elif ((capture[0] - i) % 8 == 0):
                                            l = capture[0] - 8
                                            while l > i:
                                                capture.append(l)
                                                l = l - 8
                                        else:
                                            l = capture[0] - 1
                                            while l > i:
                                                capture.append(l)
                                                l = l - 1

                                m = 0
                                while m < 64:
                                    if (m in self.figures.keys() and self.figures[m]["p"] == "B"):
                                        turns = self.getTurnsForFigureOnField(m)
                                        if (self.figures[m]["f"] == "K"):
                                            if (capture[0] in turns[1]):
                                                if (self.simulateIsChessAfterTurn(m, capture[0], 2) == False):
                                                    return False
                                        else:
                                            n = 0
                                            while n < len(capture):
                                                if (capture[n] in turns[0] or capture[n] in turns[1]):
                                                    if (self.simulateIsChessAfterTurn(m, capture[n], 2) == False):
                                                        return False
                                                n = n + 1
                                    m = m + 1
                                return True
                            else:
                                return True
                        else:
                            return False
            i = i + 1
        return False

    def simulateIsChessAfterTurn(self, startField, endField, type):
        startFigure = self.figures[startField]
        del self.figures[startField]
        deleteFigureOnEndField = False
        if (endField in self.figures.keys()):
            deleteFigureOnEndField = True
            endFigure = self.figures[endField]
            del self.figures[endField]

        data = {endField: {"p": startFigure["p"], "f": startFigure["f"]}}
        self.figures.update(data)

        self.setAllTurns()

        if(type == 1):
            schach = self.myChessControll()
        elif(type == 2):
            schach = self.chessControll()

        del self.figures[endField]
        data = {startField: {"p": startFigure["p"], "f": startFigure["f"]}}
        self.figures.update(data)
        if (deleteFigureOnEndField == True):
            data = {endField: {"p": endFigure["p"], "f": endFigure["f"]}}
            self.figures.update(data)

        return schach

    def isRochadePossible(self, turmPos):
        if(self.playerKey == "W"):
            if(turmPos == 56 or turmPos == 63):
                if(turmPos in self.gameTurns):
                    return False
                if(60 in self.gameTurns):
                    return False
                if(60 in self.allBlackDestroyTurns):
                    return False
                if(turmPos > 60):
                    i = 61
                    while i <= 62:
                        if(i in self.figures.keys()):
                            return False
                        if(i in self.allBlackNormalTurns):
                            return False
                        i = i + 1
                else:
                    i = 59
                    while i >= 58:
                        if(i in self.figures.keys()):
                            return False
                        if(i in self.allBlackNormalTurns):
                            return False
                        i = i - 1
                return True
            else:
                return False
        else:
            if(turmPos == 0 or turmPos == 7):
                if (turmPos in self.gameTurns):
                    return False
                if (4 in self.gameTurns):
                    return False
                if (4 in self.allBlackDestroyTurns):
                    return False
                if (int(turmPos) > 4):
                    i = 5
                    while i <= 6:
                        if (i in self.figures.keys()):
                            return False
                        if (i in self.allWhiteNormalTurns):
                            return False
                        i = i + 1
                else:
                    i = 3
                    while i >= 2:
                        if (i in self.figures.keys()):
                            return False
                        if (i in self.allWhiteNormalTurns):
                            return False
                        i = i - 1

                return True
            else:
                return False

    def isOnPositionFigureOfMyTeam(self, input):
        if (input in self.figures.keys()):
            if(self.figures[input]["p"] == self.playerKey) :
                return input
            else:
                print(color.redColor("No figure from your team!"))
                return False
        print(color.redColor("No figure on field!"))
        return False

    def updateFigureOnField(self, start, fin):
        if (fin in self.figures.keys()):
            del self.figures[fin]
        current = self.figures[start]
        del self.figures[start]

        data = {fin:{"p": current["p"], "f":current["f"]}}
        self.figures.update(data)

    def isValidInput(self, input):
        isField = self.getPositionToField(input)
        if(isField is False):
            print(color.redColor("This is not a valid Input!"))
            return False
        elif(isField == "message"):
            return False
        else:
            return isField

    def getPositionToField(self, raw_input):
        input = list(raw_input.lower())
        if(len(input) != 2):
            return False
        if(input[0] == 'a'):
            x = 8
        elif(input[0] == 'b'):
            x = 7
        elif(input[0] == "c"):
            x = 6
        elif(input[0] == "d"):
            x = 5
        elif(input[0] == "e"):
            x = 4
        elif(input[0] == "f"):
            x = 3
        elif(input[0] == "g"):
            x = 2
        elif(input[0] == "h"):
            x = 1
        else:
            return False

        try:
            int(input[1])
            return 72 - int(input[1]) * 8 - x
        except ValueError:
            return False

    def ifFieldInListOfColorfulBackgroundList(self, field):
        if(field in self.colorToFieldList):
            return True
        return False

    def showFieldWithColorfulBackground(self, field, text):
        colorKey = self.colorToFieldList[field]
        if(colorKey == "red"):
            return color.redBackground(text)
        if(colorKey == "yellow"):
            return color.yellowBackground(text)
        if(colorKey == "green"):
            return color.greenBackground(text)
        return color.cyanBackground(text)

    def field(self, number):
        if (int(number / 8) % 2 == 0) :
            if(number % 2 == 0):
                if(number in self.figures.keys()):
                    if(self.ifFieldInListOfColorfulBackgroundList(number) is False):
                        return color.whiteBackground(self.figures[number]["p"] + self.figures[number]["f"])
                    else:
                        return self.showFieldWithColorfulBackground(number, self.figures[number]["p"] + self.figures[number]["f"])
                else:
                    if(self.ifFieldInListOfColorfulBackgroundList(number) is False):
                        return color.whiteBackground("  ")
                    else:
                        return self.showFieldWithColorfulBackground(number, "  ")
            else:
                if(number in self.figures.keys()):
                    if(self.ifFieldInListOfColorfulBackgroundList(number) is False):
                        return color.blueBackground(self.figures[number]["p"] + self.figures[number]["f"])
                    else:
                        return self.showFieldWithColorfulBackground(number,self.figures[number]["p"] + self.figures[number]["f"])
                else:
                    if(self.ifFieldInListOfColorfulBackgroundList(number) is False):
                        return color.blueBackground("  ")
                    else:
                        return self.showFieldWithColorfulBackground(number, "  ")
        else:
            if (number % 2 == 1):

                if(number in self.figures.keys()):
                    if(self.ifFieldInListOfColorfulBackgroundList(number) is False):
                        return color.whiteBackground(self.figures[number]["p"] + self.figures[number]["f"])
                    else:
                        return self.showFieldWithColorfulBackground(number, self.figures[number]["p"] + self.figures[number]["f"])
                else:
                    if(self.ifFieldInListOfColorfulBackgroundList(number) is False):
                        return color.whiteBackground("  ")
                    else:
                        return self.showFieldWithColorfulBackground(number, "  ")
            else:
                if(number in self.figures.keys()):
                    if (self.ifFieldInListOfColorfulBackgroundList(number) is False):
                        return color.blueBackground(self.figures[number]["p"] + self.figures[number]["f"])
                    else:
                        return self.showFieldWithColorfulBackground(number,self.figures[number]["p"] + self.figures[number]["f"])
                else:
                    if(self.ifFieldInListOfColorfulBackgroundList(number) is False):
                        return color.blueBackground("  ")
                    else:
                        return self.showFieldWithColorfulBackground(number, "  ")

    def commandList(self, command):
        if (command == "/clear") :
            self.clear()
            print("Player is", self.actualPlayer)
            self.completeField()
            return
        if(command == "/ff"):
            self.clear()
            self.lose = True
            return True
        if(command == "/r") :
            self.clear()
            print("Player is", self.actualPlayer)
            self.completeField()
            self.revert = True
            return True
        return False

    def turmTurns(self, pos):
        player = self.figures[pos]["p"]
        turns = []
        normalTurns = []
        destroyTurns = []
        L = pos % 8
        O = pos / 8
        R = 7 - L
        U = 7 - O

        i = 1
        while (i <= L):
            if (pos - i not in self.figures.keys()):
                normalTurns.append(int(pos - i))
            else:
                if (self.figures[pos - i]["p"] != player):
                    destroyTurns.append(int(pos - i))
                i = L
            i = i + 1

        i = 1
        while (i <= R):
            if (pos + i not in self.figures.keys()):
                normalTurns.append(int(pos + i))
            else:
                if (self.figures[pos + i]["p"] != player):
                    destroyTurns.append(int(pos + i))
                i = R
            i = i + 1

        i = 1
        while (i <= O):
            if (pos - i * 8 not in self.figures.keys()):
                normalTurns.append(int(pos - i * 8))
            else:
                if (self.figures[pos - i * 8]["p"] != player):
                    destroyTurns.append(int(pos - i * 8))
                i = O
            i = i + 1

        i = 1
        while (i <= U):
            if (pos + i * 8 not in self.figures.keys()):
                normalTurns.append(int(pos + i * 8))
            else:
                if (self.figures[pos + i * 8]["p"] != player):
                    destroyTurns.append(int(pos + i * 8))
                i = U
            i = i + 1

        turns.append(normalTurns)
        turns.append(destroyTurns)
        return turns

    def laeuferTurns(self, pos):
        player = self.figures[pos]["p"]
        turns = []
        normalTurns = []
        destroyTurns = []
        L = pos % 8
        O = pos / 8
        R = 7 - L
        U = 7 - O

        if (O > R):
            orStart = pos - R * 7
            orLenght = R
        else:
            orStart = pos - O * 7
            orLenght = O

        if (O > L):
            olStart = pos - L * 9
            olLenght = L
        else:
            olStart = pos - O * 9
            olLenght = O

        if (U > R):
            urStart = pos + R * 9
            urLenght = R
        else:
            urStart = pos + U * 9
            urLenght = U

        if (U > L):
            ulStart = pos + L * 7
            ulLenght = L
        else:
            ulStart = pos + U * 7
            ulLenght = U

        i = orLenght
        while (i > 0):
            i = i - 1
            if (orStart + i * 7 not in self.figures.keys()):
                if (orStart + i * 7 < 64 and orStart + i * 7 >= 0):
                    normalTurns.append(int(orStart + i * 7))
            else:
                if (self.figures[orStart + i * 7]["p"] != player):
                    destroyTurns.append(int(orStart + i * 7))
                i = 0

        i = olLenght
        while (i > 0):
            i = i - 1
            if (olStart + i * 9 not in self.figures.keys()):
                if(olStart + i * 9 < 64 and olStart + i * 9 >= 0):
                    normalTurns.append(int(olStart + i * 9))
            else:
                if (self.figures[olStart + i * 9]["p"] != player):
                    destroyTurns.append(int(olStart + i * 9))
                i = 0
        i = ulLenght
        while (i > 0):
            i = i - 1
            if (ulStart - i * 7 not in self.figures.keys()):
                if(ulStart - i * 7 >= 0):
                    normalTurns.append(int(ulStart - i * 7))
            else:
                if (self.figures[ulStart - i * 7]["p"] != player):
                    destroyTurns.append(int(ulStart - i * 7))
                i = 0

        i = urLenght
        while (i > 0):
            i = i - 1
            if (urStart - i * 9 not in self.figures.keys()):
                if(urStart - i * 9 >= 0):
                    normalTurns.append(int(urStart - i * 9))
            else:
                if (self.figures[urStart - i * 9]["p"] != player):
                    destroyTurns.append(int(urStart - i * 9))
                i = 0

        turns.append(normalTurns)
        turns.append(destroyTurns)
        return turns

    def damenTurns(self, pos):
        player = self.figures[pos]["p"]
        turns = []
        normalTurns = []
        destroyTurns = []
        L = pos % 8
        O = pos / 8
        R = 7 - L
        U = 7 - O

        i = 1
        while (i <= L):
            if (pos - i not in self.figures.keys()):
                normalTurns.append(int(pos - i))
            else:
                if (self.figures[pos - i]["p"] != player):
                    destroyTurns.append(int(pos - i))
                i = L
            i = i + 1

        i = 1
        while (i <= R):
            if (pos + i not in self.figures.keys()):
                normalTurns.append(int(pos + i))
            else:
                if (self.figures[pos + i]["p"] != player):
                    destroyTurns.append(int(pos + i))
                i = R
            i = i + 1

        i = 1
        while (i <= O):
            if (pos - i * 8 not in self.figures.keys()):
                normalTurns.append(int(pos - i * 8))
            else:
                if (self.figures[pos - i * 8]["p"] != player):
                    destroyTurns.append(int(pos - i * 8))
                i = O
            i = i + 1

        i = 1
        while (i <= U):
            if (pos + i * 8 not in self.figures.keys()):
                normalTurns.append(int(pos + i * 8))
            else:
                if (self.figures[pos + i * 8]["p"] != player):
                    destroyTurns.append(int(pos + i * 8))
                i = U
            i = i + 1

        if (O > R):
            orStart = pos - R * 7
            orLenght = R
        else:
            orStart = pos - O * 7
            orLenght = O

        if (O > L):
            olStart = pos - L * 9
            olLenght = L
        else:
            olStart = pos - O * 9
            olLenght = O

        if (U > R):
            urStart = pos + R * 9
            urLenght = R
        else:
            urStart = pos + U * 9
            urLenght = U

        if (U > L):
            ulStart = pos + L * 7
            ulLenght = L
        else:
            ulStart = pos + U * 7
            ulLenght = U

        i = orLenght
        while (i > 0):
            i = i - 1
            if (orStart + i * 7 not in self.figures.keys()):
                if (orStart + i * 7 < 64 and orStart + i * 7 >= 0):
                    normalTurns.append(int(orStart + i * 7))
            else:
                if (self.figures[orStart + i * 7]["p"] != player):
                    destroyTurns.append(int(orStart + i * 7))
                i = 0

        i = olLenght
        while (i > 0):
            i = i - 1
            if (olStart + i * 9 not in self.figures.keys()):
                if(olStart + i * 9 < 64 and olStart + i * 9 >= 0):
                    normalTurns.append(int(olStart + i * 9))
            else:
                if (self.figures[olStart + i * 9]["p"] != player):
                    destroyTurns.append(int(olStart + i * 9))
                i = 0
        i = ulLenght
        while (i > 0):
            i = i - 1
            if (ulStart - i * 7 not in self.figures.keys()):
                if(ulStart - i * 7 >= 0):
                    normalTurns.append(int(ulStart - i * 7))
            else:
                if (self.figures[ulStart - i * 7]["p"] != player):
                    destroyTurns.append(int(ulStart - i * 7))
                i = 0

        i = urLenght
        while (i > 0):
            i = i - 1
            if (urStart - i * 9 not in self.figures.keys()):
                if(urStart - i * 9 >= 0):
                    normalTurns.append(int(urStart - i * 9))
            else:
                if (self.figures[urStart - i * 9]["p"] != player):
                    destroyTurns.append(int(urStart - i * 9))
                i = 0

        turns.append(normalTurns)
        turns.append(destroyTurns)
        return turns

    def koenigTurns(self, pos):
        player = self.figures[pos]["p"]
        turns = []
        normalTurns = []
        destroyTurns = []

        if (pos % 8 != 7):
            if (pos + 1 not in self.figures.keys()):
                normalTurns.append(int(pos + 1))
            else:
                if (self.figures[pos + 1]["p"] != player):
                    destroyTurns.append(int(pos + 1))
        if (pos % 8 != 0):
            if (pos - 1 not in self.figures.keys()):
                normalTurns.append(int(pos - 1))
            else:
                if (self.figures[pos - 1]["p"] != player):
                    destroyTurns.append(int(pos - 1))

        if ((pos - 8) >= 0):
            if (pos - 8 not in self.figures.keys()):
                normalTurns.append(int(pos - 8))
            else:
                if (self.figures[pos - 8]["p"] != player):
                    destroyTurns.append(int(pos - 8))
            if ((pos - 8) % 8 != 7):
                if (pos - 8 + 1 not in self.figures.keys()):
                    normalTurns.append(int(pos - 8 + 1))
                else:
                    if (self.figures[pos - 8 + 1]["p"] != player):
                        destroyTurns.append(int(pos - 8 + 1))
            if ((pos - 8) % 8 != 0):
                if (pos - 8 - 1 not in self.figures.keys()):
                    normalTurns.append(int(pos - 8 - 1))
                else:
                    if (self.figures[pos - 8 - 1]["p"] != player):
                        destroyTurns.append(int(pos - 8 - 1))

        if ((pos + 8) < 64):
            if (pos + 8 not in self.figures.keys()):
                normalTurns.append(int(pos + 8))
            else:
                if (self.figures[pos + 8]["p"] != player):
                    destroyTurns.append(int(pos + 8))
            if ((pos + 8) % 8 != 7):
                if (pos + 8 + 1 not in self.figures.keys()):
                    normalTurns.append(int(pos + 8 + 1))
                else:
                    if (self.figures[pos + 8 + 1]["p"] != player):
                        destroyTurns.append(int(pos + 8 + 1))
            if ((pos + 8) % 8 != 0):
                if (pos + 8 - 1 not in self.figures.keys()):
                    normalTurns.append(int(pos + 8 - 1))
                else:
                    if (self.figures[pos + 8 - 1]["p"] != player):
                        destroyTurns.append(int(pos + 8 - 1))

        if(pos not in self.gameTurns):
            if(self.isRochadePossible(pos + 3)):
                normalTurns.append(pos + 2)
            if(self.isRochadePossible(pos - 4)):
                normalTurns.append(pos - 2)

        turns.append(normalTurns)
        turns.append(destroyTurns)
        return turns

    def springerTurns(self, pos):
        player = self.figures[pos]["p"]
        turns = []
        normalTurns = []
        destroyTurns = []

        O = pos / 8
        U = 7 - O
        L = pos % 8
        R = 7 - L

        if (O >= 2 and R >= 1):
            if (pos - 15 not in self.figures.keys()):
                if (pos - 15 >= 0):
                    normalTurns.append(int(pos - 15))
            else:
                if (self.figures[pos - 15]["p"] != player):
                    destroyTurns.append(int(pos - 15))

        if (O >= 2 and L >= 1):
            if (pos - 17 not in self.figures.keys()):
                if (pos - 17 >= 0):
                    normalTurns.append(int(pos - 17))
            else:
                if (self.figures[pos - 17]["p"] != player):
                    destroyTurns.append(int(pos - 17))

        if (O >= 1 and L >= 2):
            if (pos - 10 not in self.figures.keys()):
                if(pos - 10 >= 0):
                    normalTurns.append(int(pos - 10))
            else:
                if (self.figures[pos - 10]["p"] != player):
                    destroyTurns.append(int(pos - 10))

        if (U >= 1 and L >= 2):
            if (pos + 6 not in self.figures.keys()):
                if(pos + 6 < 64):
                    normalTurns.append(int(pos + 6))
            else:
                if (self.figures[pos + 6]["p"] != player):
                    destroyTurns.append(int(pos + 6))

        if (U >= 2 and L >= 1):
            if (pos + 15 not in self.figures.keys()):
                if(pos + 15 < 64):
                    normalTurns.append(int(pos + 15))
            else:
                if (self.figures[pos + 15]["p"] != player):
                    destroyTurns.append(int(pos + 15))

        if (U >= 2 and R >= 1):
            if (pos + 17 not in self.figures.keys()):
                if(pos + 17 < 64):
                    normalTurns.append(int(pos + 17))
            else:
                if (self.figures[pos + 17]["p"] != player):
                    destroyTurns.append(int(pos + 17))

        if (U >= 1 and R >= 2):
            if (pos + 10 not in self.figures.keys()):
                if(pos + 10 < 64):
                    normalTurns.append(pos + 10)
            else:
                if (self.figures[pos + 10]["p"] != player):
                    destroyTurns.append(pos + 10)

        if (O >= 1 and R >= 2):
            if (pos - 6 not in self.figures.keys()):
                if(pos - 6 >= 0):
                    normalTurns.append(pos - 6)
            else:
                if (self.figures[pos - 6]["p"] != player):
                    destroyTurns.append(pos - 6)

        turns.append(normalTurns)
        turns.append(destroyTurns)
        return turns

    def bauernTurns(self, pos):
        player = self.figures[pos]["p"]
        turns = []
        normalTurns = []
        destroyTurns = []

        if (player == "W"):
            if (pos > 47):
                max = 2
            else:
                max = 1
            i = 1
            while (i <= max):
                if (pos - i * 8 >= 0):
                    if (pos - i * 8 not in self.figures.keys()):
                        normalTurns.append(int(pos - i * 8))
                        i = i + 1
                    else:
                        i = 100
                else:
                    i = i + 1
            if ((pos - 8) % 8 == 0):
                if (pos - 7 >= 0):
                    if (pos - 7 in self.figures.keys()):
                        if (self.figures[pos - 7]["p"] != player):
                            destroyTurns.append(int(pos - 7))
            elif ((pos - 8) % 8 == 7):
                if (pos - 9 >= 0):
                    if (pos - 9 in self.figures.keys()):
                        if (self.figures[pos - 9]["p"] != player):
                            destroyTurns.append(int(pos - 9))
            else:
                if (pos - 9 >= 0):
                    if (pos - 9 in self.figures.keys()):
                        if (self.figures[pos - 9]["p"] != player):
                            destroyTurns.append(int(pos - 9))
                if (pos - 7 >= 0):
                    if (pos - 7 in self.figures.keys()):
                        if (self.figures[pos - 7]["p"] != player):
                            destroyTurns.append(int(pos - 7))
        else:
            if (pos < 16):
                max = 2
            else:
                max = 1
            i = 1
            while (i <= max):
                if (pos + i * 8 < 64):
                    if (pos + i * 8 not in self.figures.keys()):
                        normalTurns.append(int(pos + i * 8))
                        i = i + 1
                    else:
                        i = 100
                else:
                    i = i + 1
            if ((pos + 8) % 8 == 0):
                if (pos + 9 < 64):
                    if (pos + 9 in self.figures.keys()):
                        if (self.figures[pos + 9]["p"] != player):
                            destroyTurns.append(int(pos + 9))
            elif ((pos + 8) % 8 == 7):
                if (pos + 7 < 64):
                    if (pos + 7 in self.figures.keys()):
                        if (self.figures[pos + 7]["p"] != player):
                            destroyTurns.append(int(pos + 7))
            else:
                if (pos + 7 < 64):
                    if (pos + 7 in self.figures.keys()):
                        if (self.figures[pos + 7]["p"] != player):
                            destroyTurns.append(int(pos + 7))
                if (pos + 9 < 64):
                    if (pos + 9 in self.figures.keys()):
                        if (self.figures[pos + 9]["p"] != player):
                            destroyTurns.append(int(pos + 9))

        turns.append(normalTurns)
        turns.append(destroyTurns)
        return turns

    @staticmethod
    def clear():
        try:
            system("clear")
        except ValueError:
            print()

game = Game()