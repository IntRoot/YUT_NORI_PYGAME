

import pygame
import random
import os
import sys
from components.textbox import TextBox 

# Add the parent directory of the current file to the system path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)


class Yut:
    def __init__(self):
        self.yut_side = None
        self.creation_time = pygame.time.get_ticks() 
        
      
    def flip_yut(self):
        self.yut_side = random.choice(['front', 'back'])

    def is_done(self):
        elapsed_time = pygame.time.get_ticks() - self.creation_time
        return elapsed_time > 1000
    
class YutGame:
    def __init__(self):
        self.yuts_list = [Yut() for i in range(4)]
        self.move = 0
        self.front_count = 0
        self.text = ''
        self.one_more = False


    def flip_all_yuts(self):
        for yut in self.yuts_list:
            yut.flip_yut()


    def count_yuts_front(self):
        self.front_count = 0
        for yut in self.yuts_list:
            if yut.yut_side == 'front':
                self.front_count += 1
        return self.front_count
    
    

    def decide_moves(self):
        print(self.front_count, 'front count')
        if self.front_count == 0:
            self.one_more = True
            self.move = 5
            self.text = 'MO'
        elif self.front_count == 1:
            self.move = 1
            self.text = 'DO'
        elif self.front_count == 2:
            self.move = 2
            self.text = 'GAE'
        elif self.front_count == 3:
            self.move = 3
            self.text = 'GEOL'
        elif self.front_count == 4:
            self.move = 4
            self.text = 'YUT'
            self.one_more = True
            
        return self.move
    
    def draw(self, screen, current_player):

        yut_front = pygame.transform.scale(pygame.image.load(os.path.join(parent_dir, 'images', 'yut_front.png') ), (550, 550)) 
        yut_front = pygame.transform.scale(yut_front, (550, 550))  # Scale the image
        yut_back = pygame.image.load(os.path.join(parent_dir, 'images', 'yut_back.png'))
        yut_back = pygame.transform.scale(yut_back, (700, 700))
      
    
        for i, yut in enumerate(self.yuts_list):
                if yut.is_done():
                    yut_image = yut_front if yut.yut_side == 'front' else yut_back
                    screen.blit(yut_image, (i*95, 100))
            
        if current_player == 'tiger':
                textbox_bg_color = 'black'  # black
                textbox_text_color = 'white'  # white
        else:
                textbox_bg_color = 'white'  # white
                textbox_text_color = 'black'  # black

            # create the textbox with the desired background and text color
        textbox = TextBox(self.text, size=(80, 50), font_size=24, bg_color=textbox_bg_color,
                            text_color=textbox_text_color)

        textbox.rect.x = 800
        textbox.rect.y = 600
        textbox.update()
        screen.blit(textbox.image, textbox.rect)
    
        
