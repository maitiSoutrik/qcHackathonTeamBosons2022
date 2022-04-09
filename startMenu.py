import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600,400))

def startGame():
    pass

menu = pygame_menu.Menu('Welcome',
                        400,
                        300,
                        theme=pygame_menu.themes.THEME_DARK)

menu.add.button('Play', startGame)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)