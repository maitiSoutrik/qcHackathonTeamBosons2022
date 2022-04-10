from sympy import true
import os
import sys
import pygame

screen = pygame.display.set_mode((800,600))
tools = pygame.image.load("tools.png")
toolsX = 10
toolsY = 10
pos1 = [toolsX,toolsY]
# TODO : Add logic gate objects in the view
# The objects should be clickable and dragable
#

class gateObject(object):
    SIZE = (150, 150)
    
    def __init__(self, pos):
        self.rect = pygame.Rect((0,0), gateObject.SIZE)
        self.rect.center = pos
        # self.text, self.text_rect = self.setup_font()
        self.click = False

    # def setup_font(self):
    #     font = pygame.font.SysFont('timesnewroman', 30)
    #     message = "I'm a red square"
    #     label = font.render(message, True, pygame.Color("white"))
    #     label_rect = label.get_rect()
    #     return label, label_rect

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.click = True
            pygame.mouse.get_rel()

    def update(self, screen_rect):
        if self.click:
            self.rect.move_ip(pygame.mouse.get_rel())
            self.rect.clamp_ip(screen_rect)
        # self.text_rect.center = (self.rect.centerx, self.rect.centery+90)

    def draw(self, surface):
        surface.fill(pygame.Color("red"), self.rect)
        # surface.blit(self.text, self.text_rect)




class HGate(gateObject):
    def __init__(self, pos):
        super().__init__(pos)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.click = True
            pygame.mouse.get_rel()

    def update(self, screen_rect):
        if self.click:
            self.rect.move_ip(pygame.mouse.get_rel())
            self.rect.clamp_ip(screen_rect)
        # self.text_rect.center = (self.rect.centerx, self.rect.centery+90)


    def draw(self, surface):
        surface.fill(pygame.Color("blue"), self.rect)
        # surface.blit(self.text, self.text_rect)

    
    
class CNOTGate(gateObject):
    def __init__(self, pos):
        super().__init__(pos)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.click = True
            pygame.mouse.get_rel()

    def update(self, screen_rect):
        if self.click:
            self.rect.move_ip(pygame.mouse.get_rel())
            self.rect.clamp_ip(screen_rect)
        # self.text_rect.center = (self.rect.centerx, self.rect.centery+90)

    def draw(self, surface):
        surface.fill(pygame.Color("green"), self.rect)
        # surface.blit(self.text, self.text_rect)


class XGate(gateObject):
    def __init__(self, pos):
        super().__init__(pos)

    def check_click(self, pos):
        if self.rect.collidepoint(pos):
            self.click = True
            pygame.mouse.get_rel()

    def update(self, screen_rect):
        if self.click:
            self.rect.move_ip(pygame.mouse.get_rel())
            self.rect.clamp_ip(screen_rect)
        # self.text_rect.center = (self.rect.centerx, self.rect.centery+90)

    def draw(self, surface):
        surface.fill(pygame.Color("yellow"), self.rect)
        # surface.blit(self.text, self.text_rect)


class level1Window():
    def __init__(self) -> None:
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.done = False
        self.keys = pygame.key.get_pressed()
        self.gate1 = HGate(self.screen_rect.center)
        self.gate2 = XGate(self.screen_rect.center)
        self.gate3 = CNOTGate(self.screen_rect.center)


    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                self.done = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.gate1.check_click(event.pos)
                self.gate2.check_click(event.pos)
                self.gate3.check_click(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.gate1.click = False
                self.gate2.click = False
                self.gate3.click = False
                
            elif event.type in (pygame.KEYUP, pygame.KEYDOWN):
                self.keys = pygame.key.get_pressed() 

    def render(self):
        self.screen.fill(pygame.Color("black"))
        self.gate1.draw(self.screen)
        self.gate2.draw(self.screen)
        self.gate3.draw(self.screen)
        pygame.display.update()

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.gate1.update(self.screen_rect)
            self.gate2.update(self.screen_rect)
            self.gate3.update(self.screen_rect)
            self.render()
            self.clock.tick(self.fps)


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    # pygame.init()
    # pygame.display.set_caption(CAPTION)
    # pygame.display.set_mode(SCREEN_SIZE)
    level1Window().main_loop()
    pygame.quit()
    sys.exit()
    

if __name__ == "__main__":
    main()





