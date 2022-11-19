import pygame



class Button():
    def __init__(self, image, x, y, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def render_image_button(self, surface):
        # action = what should happen when clicked (determined in main)
        action = False

        pos = pygame.mouse.get_pos()

        # pos over button and clicked?
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and self.clicked == False:

                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0]== False:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        # returns true or false
        return action