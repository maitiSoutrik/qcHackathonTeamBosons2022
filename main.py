import pygame
import startMenu
import game
import pygame_menu

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Adventures of the Quantum Dungeons")
icon = pygame.image.load("quantum-computing.png")
pygame.display.set_icon(icon)




startMenu.menuItems.startScreen()

running = True


    


