from sympy import true
import pygame

screen = pygame.display.set_mode((800,600))
tools = pygame.image.load("tools.png")

# TODO : Add logic gate objects in the view


toolsX = 10
toolsY = 10

class level1():
    def startGame():
        running = true
        
        while running:
            screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            level1.toolsIcon()
            pygame.display.update()

    def toolsIcon():
        screen.blit(tools, (toolsX, toolsY))
