import pygame

# used for idle animation and maybe attacks from enemies (if we want to)
class ImageAnimation():
    def __init__(self, image_list, x, y, scale):
        self.scale = scale
        self.image_list = image_list
        self.current_image = 0
        self.done = False

        image = self.image_list[int(self.current_image)]
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def play_animation(self, surface, images_per_frame, loop):
        self.loop = loop
        if not self.done:
            self.update_animation(surface, images_per_frame)  # Update the animation until it is done

    def reset_animation(self):
        self.current_image = 0
        self.done = False

    def update_animation(self, surface, images_per_frame):

        if self.current_image >= len(self.image_list):

            if self.loop == True:
                self.reset_animation()
            else:
                self.done = True
                return

        # needs to get new values since the images have different sizes
        image = self.image_list[int(self.current_image)]
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * self.scale), int(height * self.scale)))

        surface.blit(self.image, (self.rect.x, self.rect.y))

        # speed controller
        self.current_image += images_per_frame


    def make_button(self):
        pass

    def move_image(self):
        pass


# not sure when to use this
class TextAnimation():
    def __init__(self, text_list, x, y, color, font, font_size):
        self.color = color
        self.font_size = font_size
        self.text_list = text_list
        self.current_text = 0
        self.font = pygame.font.Font(font, font_size)

        self.text = self.font.render(text_list[int(self.current_text)], True, color)
        self.rect = self.text.get_rect()
        self.rect.topleft = (x, y)
        self.done = False

    def play_animation(self, surface, images_per_frame, loop):
        self.loop = loop
        if not self.done:
            self.update_animation(surface, images_per_frame)

    def reset_animation(self):
        self.current_text = 0
        self.done = False

    def update_animation(self, surface, images_per_frame):
        if self.current_text >= len(self.text_list):
            if self.loop == True:
                self.reset_animation()
            else:
                self.done = True
                return

        self.text = self.font.render(self.text_list[int(self.current_text)], True, self.color)

        surface.blit(self.text, (self.rect.x, self.rect.y))
        self.current_text += images_per_frame
    def make_button(self):
        pass

    def move_text(self):
        pass

