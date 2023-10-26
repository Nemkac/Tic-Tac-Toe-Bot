import copy
from Bot import *
from board import *
import pygame

class Game:
    def __init__(self, display):
        self.display = display
        self.board = Board()
        self.player = 1
        self.BOT = Bot()
        self.running = True
        self.DrawBoard()

    def DrawBoard(self):
        self.display.blit(boardImage, (0, 0))

    def SwitchPlayer(self):
        if self.player == 1:
            self.player = 2
        elif self.player == 2:
            self.player = 1

    def PlaceSign(self, x, y, player):
        if player == 1:        
            self.display.blit(Ximg, (y * boardField + 55,x * boardField + 55))

        if player == 2:
            self.display.blit(Oimg, (y * boardField + 60, x * boardField + 60))
            
    def RestartGame(self):
        self.__init__(self.display)
    
    def EndGame(self):
        if self.board.Result(True) != 0  or self.board.IsBoardFull():
            return True
        else:
            return False