import pygame

class Animation():
    def __init__(self, image_list, x, y, scale):
        self.scale = scale
        self.image_list = image_list
        self.current_image = 0

        image = self.image_list[int(self.current_image)]
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, surface, images_per_frame):

        if self.current_image >= len(self.image_list):
            self.current_image = 0

        image = self.image_list[int(self.current_image)]
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))

        surface.blit(self.image, (self.rect.x, self.rect.y))

        self.current_image += images_per_frame


    def make_button(self):
        pass