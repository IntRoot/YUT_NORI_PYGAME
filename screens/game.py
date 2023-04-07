import pygame
import random
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# from components import Shape, TextBox
# from components.yut import Yut
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
        self.current_player_idx = 0 
        self.init_tokens()
        self.opponent_tiger = Player(self.board, self.tokens[0])
        self.user = Player(self.board, self.tokens[1])
        self.user_played = False
    
       

        

    
    def init_tokens(self):
        token_images = ['tiger_token.png', 'user.png']
        ### add normal user later
        for i, player in enumerate(self.players):
            token_image = token_images[i]
            token = Token(80, 80, token_image, player)
            self.tokens.append(token)
    

    def draw(self):
        """Draws the screen"""
        self.screen.blit(self.background, (0, 0))
        # self.board.draw()
        for token in self.tokens:
            token.draw()
 
       
            if token.winner:
                    textbox = TextBox(f"{token.winner} wins!", size=(600, 100), font_size=20, bg_color='black', text_color='white')
                    textbox.rect.x = (self.screen.get_width() // 2) - (textbox.rect.width // 2)  # Center textbox horizontally
                    textbox.rect.y = (self.screen.get_height() // 2) - (200 // 2)

                    textbox.update()
                    self.screen.blit(textbox.image, textbox.rect)
                    pygame.display.update()
    
                    self.back_button = Button(600, 100, "Back to Welcome Screen")
                    self.back_button.rect.x = (self.screen.get_width() // 2) - (self.back_button.rect.width // 2)
                    self.back_button.rect.y = (self.screen.get_height() // 2) + 100
                    self.back_button.update()
                    self.screen.blit(self.back_button.image, self.back_button.rect)
                    pygame.display.update()
      

    # Update the display
        pygame.display.flip()



    def switch_player(self):
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

    def play_tiger(self):
    
        self.opponent_tiger.play(self.yut_game)
        print('tiger moved')
        self.yut_game.draw(self.screen, self.players[self.current_player_idx])

       
        pygame.display.update()
        pygame.time.delay(1000)
        self.switch_player()
    
       
        

    def play_user(self, event):

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.user.play(self.yut_game)
            self.yut_game.draw(self.screen, self.players[self.current_player_idx])
            pygame.display.update()
            pygame.time.delay(1000)
            print('player moved')
            
            self.user_played = True
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
                pygame.display.update()  # update the display
                self.user_played = False 
        
        for token in self.tokens:
             if token.winner:
                if event.type == pygame.MOUSEBUTTONDOWN and self.back_button.rect.collidepoint(event.pos):
                        from screens.welcome import WelcomeScreen
                        screen = WelcomeScreen(self.screen)
                        screen.run()
                        self.__init__(self.screen) 
                        
                     
                        
                        
                       
        ### stop movement when winner decides if winne is not decide ignore mouse movement
        ## yot mo
        ## close game screen
  

    
 
            