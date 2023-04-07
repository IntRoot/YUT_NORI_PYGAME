import pygame


class TextBox(pygame.sprite.Sprite):
    def __init__(self, value='', size=(50, 50), font_size=24, bg_color=(255, 255, 255), text_color=(0, 0, 0)):
        super().__init__()
        self.value = value
        self.bg_color = bg_color
        self.text_color = text_color

        pygame.font.init()
        self.image = pygame.Surface(size)
        self.font = pygame.font.Font(pygame.font.get_default_font(), font_size)
        self.rect = self.image.get_rect()

    def update(self):
        font_surface = self.font.render(str(self.value), True, self.text_color)
        self.image.fill((self.bg_color))
        text_rect = font_surface.get_rect(center=self.image.get_rect().center)
        self.image.blit(font_surface, text_rect)

