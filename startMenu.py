import pygame
import pygame_menu
import game
class menuItems():
    

    # Create the start Screen
    def startScreen():
        menu = pygame_menu.Menu('Welcome',
                            800,
                            600,
                            theme=pygame_menu.themes.THEME_DARK)
        screen = pygame.display.set_mode((800,600))
        menu.add.button('Play', game.level1.startGame)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(screen)
