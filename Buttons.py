import pygame


class Button():
    def __init__(self, image, x, y, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicking = False

    def got_pressed(self):
        # on release
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

    def mouse_hover(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True

    def render_image(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))