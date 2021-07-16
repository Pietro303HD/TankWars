from .. import game
import pygame
def sizedraw(screen, sprite, size, pos):
	screen.blit(pygame.transform.scale(sprite, (game.size * size[0],game.size * size[1])), (pos[0] * game.size, pos[1] * game.size))