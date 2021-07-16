import pygame
import time
from assets import assets
from src.engine import *
pygame.init()

class Tank:
    def __init__(self, pos):
        self.pos = pos
        self.moveables = [(0,0),(0,1),(0,-1),(0,2),(0,-2),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1),(-2,0),(2,0)]
    def moveable(self, pos):
        for tile in self.moveables:
            if (self.pos.x + tile[0], self.pos.y + tile[1]) == pos:
                return True
        return False

def matchlist(array, matcher):
    for obj in array:
        if obj == matcher:
            return True
    return False

def get(path, x, y):
    image = pygame.Surface((16,16), pygame.SRCALPHA).convert_alpha()
    image.fill((255,0,0,0))
    image.blit(path, (0,0), (x * 16,y * 16,16,16))
    return image

def gameRun():
    running = True
    starts = 0
    screen = topdownscreen(20,20,32)
    tank = Tank(pygame.Vector2(7,7))
    units = [tank]
    selected = 0
    while running:
        mousepos = pygame.mouse.get_pos()
        tilemousepos = pygame.Vector2(int(mousepos[0] / 32), int(mousepos[1] / 32))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(int(tilemousepos.distance_to(tank.pos)))
                if units[selected].moveable(tilemousepos):
                    units[selected].pos = tilemousepos
        screen.fill((255,255,255))

        for tile in range(20):
            for tilex in range(20):
                draw(screen, assets.grass, (tilex, tile))


        c = (mousepos[0], int(mousepos[0] / 32))

        surf = pygame.Surface((20 * 32, 20 * 32), pygame.SRCALPHA).convert_alpha()
        surf.set_alpha(125)
        for pos in tank.moveables:
            draw(surf, assets.moveable, (int(units[selected].pos.x) + pos[0], int(units[selected].pos.y) + pos[1]))
        screen.blit(surf, (0,0))

        draw(screen, hue(get(assets.tank, 0,0), 0), (int(units[selected].pos.x), units[selected].pos.y))
        draw(screen, get(assets.tank, 0,1), (int(units[selected].pos.x), units[selected].pos.y))
        pygame.display.flip()
