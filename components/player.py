from components.token import Token
import random
import pygame
from components.yut import YutGame
from components.textbox import TextBox

class Player:
    def __init__(self, board, token):
        self.board = board
        self.token = token  
        self.moves = 0
   
    def play(self, yut_game):
        yut_game.flip_all_yuts()
        yut_game.count_yuts_front()
        self.moves = yut_game.decide_moves()
        self.token.move(self.moves)
        

