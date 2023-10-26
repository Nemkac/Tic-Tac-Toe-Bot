import sys
import pygame
import numpy as np
import math

from game import *


def main():
    pygame.init()
    display = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("TIC-TAC-TOE")
    display.fill(backgroundColor)

    game = Game(display)
    board = game.board
    bot = game.BOT

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.RestartGame()
                    board = game.board
                    bot = game.BOT

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                x = pos[1] / boardField
                y = pos[0] / boardField

                fieldX = math.ceil(x - 1)
                fieldY = math.ceil(y - 1)

                if board.EmptySquare(fieldX, fieldY) and game.running:
                    board.MarkField(fieldX, fieldY, game.player)
                    game.PlaceSign(fieldX, fieldY, game.player)
                    game.SwitchPlayer()

                    if game.EndGame():
                        game.running = False

                    #emptyFields = game.board.GetEmptyBoardFields()

                    #for field in emptyFields:
                    #    print(field)

                    #print(game.board.boardFields)

        if game.player == bot.player and game.running:
            pygame.display.update()

            row, column = bot.Evaluation(board, alpha=float('-inf'), beta=float('inf'))
            #row, column = bot.EvaluationMinimax(board)
            game.board.MarkField(row, column, bot.player)
            game.PlaceSign(row, column, bot.player)
            game.SwitchPlayer()

            if game.EndGame():
                game.running = False

        pygame.display.update()


main()