import pygame


class TextButton():
    def __init__(self, x, y, text, color, font):
        font = pygame.font.Font(font, 100)
        self.text = font.render(text, True, color )
        self.rect = self.text.get_rect()
        self.rect.topleft = (x, y)


    def render_text_button(self, surface):

        action = False

        pos = pygame.mouse.get_pos()

        # pos over button and clicked?
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False

        surface.blit(self.text, (self.rect.x, self.rect.y))

        # returns true or false
        return action

