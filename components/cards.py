from components.button import Button
import os
import pygame
import random

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

class Card:
    def __init__(self, screen):
        self.width = 600
        self.height = 600
        self.screen = screen
        self.choices1 = Button(200, 50, "choices 1")
        self.choices2 = Button(200, 50, "choices 2")

    def draw_card(self):
        card_image = pygame.transform.scale(pygame.image.load(os.path.join(parent_dir, 'images', 'cards', 'dorong.png')), (200, 200))
        center_x = self.screen.get_width() // 2
        center_y = self.screen.get_height() // 2
        card_x = center_x - card_image.get_width() // 2
        card_y = center_y - card_image.get_height() // 2
        button_x = center_x - self.choices1.image.get_width() // 2
        button_y1 = self.screen.get_height() - 250
        button_y2 = self.screen.get_height() - 200
        self.screen.blit(card_image, (card_x, card_y))
        self.screen.blit(self.choices1.image, (button_x, button_y1))
        self.screen.blit(self.choices2.image, (button_x, button_y2))
        pygame.display.flip()
        pygame.time.wait(3000)
