import pygame.font


class Button:

    def __init__(self, ai_game, msg, position=None):
        # Button attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions/properties
        self.width, self.height = 200, 50
        self.button_color = (87, 168, 255)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build button and center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if position:
            self.rect.center = position
        else:
            self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
