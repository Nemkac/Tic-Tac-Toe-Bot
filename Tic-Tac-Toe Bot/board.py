import numpy as np
import pygame

screenWidth = 850
screenHeight = 850

rows = 3
columns = 3

boardField = 800 // columns

#COLORS
backgroundColor = (39, 60, 117)
boardLinesColor = (25, 42, 86)
circleColor = (245, 246, 250)
xColor = (232, 65, 24)
oColor = (252, 197, 49)


#boardImage = pygame.image.load("C:\\Users\\Nemanja\\Desktop\\Tic-Tac-Toe Bot\\images\\Tabla.PNG")
#Ximg = pygame.transform.scale(pygame.image.load("C:\\Users\\Nemanja\\Desktop\\Tic-Tac-Toe Bot\\images\\x.png"), (200, 200))
#Oimg = pygame.transform.scale(pygame.image.load("C:\\Users\\Nemanja\\Desktop\\Tic-Tac-Toe Bot\\images\\O.png"), (200, 200))

boardImage = pygame.image.load("C:\\Users\\Andrea\\Documents\\GitHub\\Tic-Tac-Toe-Bot\\Tic-Tac-Toe Bot\\images\\Tabla.PNG")
Ximg = pygame.transform.scale(pygame.image.load("C:\\Users\\Andrea\\Documents\\GitHub\\Tic-Tac-Toe-Bot\\Tic-Tac-Toe Bot\\images\\x.png"), (200, 200))
Oimg = pygame.transform.scale(pygame.image.load("C:\\Users\\Andrea\\Documents\\GitHub\\Tic-Tac-Toe-Bot\\Tic-Tac-Toe Bot\\images\\O.png"), (200, 200))

class Board():
    def __init__(self):
        self.boardFields = np.zeros((rows, columns))
        self.emptyBoardFields = self.boardFields
        self.markedBoardFields = 0
        self.display = None


    def MarkField(self, row, column, player):
        self.boardFields[row][column] = player
        self.markedBoardFields = self.markedBoardFields + 1

    def EmptySquare(self, row, col):
        if self.boardFields[row][col] == 0:
            return True
        else:
            return False
    
    def IsBoardFull(self):
        if self.markedBoardFields == 9:
            return True
        else: 
            return False
        
    def VerticalWinCheck(self, col):
        return self.boardFields[0][col] == self.boardFields[1][col] == self.boardFields[2][col] != 0
    
    def HorizontalWinCheck(self, row):
        return self.boardFields[row][0] == self.boardFields[row][1] == self.boardFields[row][2] != 0
    
    def DiagonalWinCheck(self, row, col):
        if self.boardFields[0][0] == self.boardFields[1][1] == self.boardFields[2][2] != 0:
            return 1
        elif self.boardFields[2][0] == self.boardFields[1][1] == self.boardFields[0][2] != 0:
            return 2

    def Result(self, gameOver = False):
        for col in range(columns):
            if self.VerticalWinCheck(col):
                #if gameOver:
                #    if self.boardFields[0][col] == 2:
                #        color = oColor
                #    else:
                #        color = xColor

                #    finalPositionStart = (col * boardField + boardField // 2, 20)
                #    finalPositionEnd = (col*boardField + boardField // 2, screenHeight - 20)

                #    pygame.draw.line(self.display, color, finalPositionStart, finalPositionEnd, 20)
                
                winner = self.boardFields[0][col]
                return winner
            
        for row in range(rows):
            if self.HorizontalWinCheck(row):
                #if gameOver:
                    #if self.boardFields[0][row] == 2:
                    #     color = oColor
                    #else:
                    #    color = xColor

                    #finalPositionStart = (20, row * boardField + boardField // 2)
                    #finalPositionEnd = (screenWidth - 20, row*boardField + boardField // 2,)

                    #pygame.draw.line(self.display, color, finalPositionStart, finalPositionEnd, 20)

                winner = self.boardFields[row][0]
                return winner
            
        for row in range(rows):
            for col in range(columns):
                if self.DiagonalWinCheck(row, col) == 1:
                    winner = self.boardFields[row][col]
                    return winner
                if self.DiagonalWinCheck(row, col) == 2:
                    winner = self.boardFields[row + 2][col]
                    return winner

        return 0

    def IsBoardEmpty(self):
        if self.markedBoardFields == 0:
            return True
        else:
            return False
        
    def GetEmptyBoardFields(self):
        emptyFields = []
        for i in range(rows):
            for j in range(columns):
                if self.boardFields[i][j] == 0:
                    emptyFields.append((i, j))

        return emptyFields