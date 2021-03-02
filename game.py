import pygame
pygame.init()

game = pygame.display.set_mode(size = (640,640))

pygame.display.set_caption("GAME")
Backgroundg = pygame.image.load('cavemen.png')


def loadgBG():
    game.blit(Backgroundg,(0,0))
    
    pygame.display.update()


loadgBG()
pygame.diplay.update()
