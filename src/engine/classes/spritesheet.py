import pygame

class SpriteSheet:
    def __init__(self, path):
        self.sheet = path
    def get(self, x, y):
        image = pygame.Surface((16,16))
        image.blit(self.sheet, (0,0), (x * 16,y * 16,16,16))
        return image
