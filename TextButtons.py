import pygame


class TextButton():
    def __init__(self, x, y, text, color, font, size):

        font = pygame.font.Font(font, size)
        self.text = font.render(text, True, color)
        self.rect = self.text.get_rect()
        self.rect.topleft = (x, y)
        self.clicking = False

    def text_button_got_pressed(self):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True:
                self.clicking = True
            if pygame.mouse.get_pressed()[0] == False:
                if self.clicking == True:
                    self.clicking = False
                    return True
                self.clicking = False
        else:
            self.clicking = False

        return False

    def render_text(self, surface):
        surface.blit(self.text, (self.rect.x, self.rect.y))