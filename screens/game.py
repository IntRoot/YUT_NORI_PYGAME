import cv2
import pygame
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
from screens.base_screen import BaseScreen
from components.board import YutNoriBoard
from components.yut import Yut, YutGame
from components.token import Token
from components.button import Button
from components.textbox import TextBox
from components.player import Player

class GameScreen(BaseScreen):
    def __init__(self, window):
        super().__init__(window)
        
        self.board = YutNoriBoard(1000,800)
        self.yut_game = YutGame()
        self.screen = window
        self.current_token_pos = 0
        self.tokens = []
        self.players = ['tiger', 'user']
        self.current_player_idx = 1
        self.init_tokens()
        self.opponent_tiger = Player(self.board, self.tokens[0])
        self.user = Player(self.board, self.tokens[1])
        self.user_played = False
        self.tiger_effect = cv2.VideoCapture(os.path.join(parent_dir, 'images', 'tiger_effect.mp4'))
        self.tiger_effect_frames = []
        self.load_tiger_effect_frames()

    def load_tiger_effect_frames(self):
        success, frame = self.tiger_effect.read()
        while success:
            frame = cv2.resize(frame, (200, 100))
            frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE) 
            frame = cv2.flip(frame, 0) # rotate the frame
            self.tiger_effect_frames.append(frame)
            success, frame = self.tiger_effect.read()

    def init_tokens(self):
        token_images = ['tiger_token.png', 'user.png']
        for i, player in enumerate(self.players):
            token_image = token_images[i]
            token = Token(80, 80, token_image, player)
            self.tokens.append(token)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        for token in self.tokens:
            token.draw()
            if token.winner:
                textbox = TextBox(f"{token.winner} wins!", size=(600, 100), font_size=20, bg_color='black', text_color='white')
                textbox.rect.x = (self.screen.get_width() // 2) - (textbox.rect.width // 2)
                textbox.rect.y = (self.screen.get_height() // 2) - (200 // 2)
                textbox.update()
                self.screen.blit(textbox.image, textbox.rect)
                self.back_button = Button(600, 100, "Back to Welcome Screen")
                self.back_button.rect.x = (self.screen.get_width() // 2) - (self.back_button.rect.width // 2)
                self.back_button.rect.y = (self.screen.get_height() // 2) + 100
                self.screen.blit(self.back_button.image, self.back_button.rect)
                pygame.display.update()

    def switch_player(self):
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

    def play_tiger(self):
        if self.tokens[0].winner != 'tiger' and  self.tokens[1].winner != 'user':
            for frame in self.tiger_effect_frames:
                self.screen.blit(pygame.surfarray.make_surface(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)), (800, 100))
                pygame.display.update()
                pygame.time.delay(50)
                
            self.opponent_tiger.play(self.yut_game)
            self.yut_game.draw(self.screen, self.players[self.current_player_idx])
            pygame.display.update()
            pygame.time.delay(1000)

            if self.opponent_tiger.moves == 4 or self.opponent_tiger.moves == 5:
                self.yut_game.one_more = False
                self.opponent_tiger.play(self.yut_game)
                self.yut_game.draw(self.screen, self.players[self.current_player_idx])
                pygame.display.update()
                pygame.time.delay(1000)
                
            if self.tokens[0].collides_with(self.tokens[1]):
                print('Tiger got you')
                self.tokens[0].winner = 'tiger'
            else:
                self.switch_player()
        
     
    

    def play_user(self, event):

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.current_player_idx == 1:
            self.user.play(self.yut_game)
            self.yut_game.draw(self.screen, self.players[self.current_player_idx])
            pygame.display.update()
            pygame.time.delay(1000)
            print('player moved')

            if self.user.moves == 4 or self.user.moves == 5:
               
                self.user.play(self.yut_game)
                self.yut_game.draw(self.screen, self.players[self.current_player_idx])
                pygame.display.update()
                pygame.time.delay(1000)
    
            self.user_played = True

            if self.tokens[1].collides_with(self.tokens[0]):
                print('Player collided with tiger!')
                self.current_player_idx = 1  # Player gets one more turn
            else:
                self.switch_player()
            
  


    def manage_event(self, event):
        
        if self.current_player_idx == 0:
            self.play_tiger()
            

        else:
            self.play_user(event)
            if self.user_played:  # check if the user has played
                self.draw()  # redraw the screen
                for token in self.tokens:
                    token.draw()  # redraw the tokens
                pygame.display.update()  
                self.user_played = False 
        
        for token in self.tokens:
             if token.winner:
                if event.type == pygame.MOUSEBUTTONDOWN and self.back_button.rect.collidepoint(event.pos):
                        from screens.welcome import WelcomeScreen
                        screen = WelcomeScreen(self.screen)
                        screen.run()
                        self.__init__(self.screen) 
                        
                     
                        
                        
                       
    

    
 
            