import pygame
import math


class Ship:
    def __init__(self, ai_game):

        # Initiate the ship and its starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load ship1.png and get rects (x,y)
        self.image = pygame.image.load(
            "Part II - Projects/Alien Invasion/alien_invasion/images/ship1.png")
        self.original_image = self.image  # Save the original image
        self.rect = self.image.get_rect()

        # Ship starts in the center/bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # Decimal values for ship movement in x and y directions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Angle of rotation (0 degrees is facing up)
        self.angle = 0

        # Set flags for continuous movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # Update the rotation angle based on the movement flags
        if self.moving_right:
            self.angle -= self.settings.ship_rotation_speed
        if self.moving_left:
            self.angle += self.settings.ship_rotation_speed

        # Rotate the ship image
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Update the y position based on the movement flags
        if self.moving_up:
            # Move the ship forward in the direction it's facing
            radians = math.radians(self.angle)
            self.x -= self.settings.ship_speed * math.sin(radians)
            self.y -= self.settings.ship_speed * math.cos(radians)
        if self.moving_down:
            # Move the ship backward in the direction it's facing
            radians = math.radians(self.angle)
            self.x += self.settings.ship_speed * math.sin(radians)
            self.y += self.settings.ship_speed * math.cos(radians)

        if self.rect.left < 0:
            self.x = self.rect.width
        if self.rect.right > self.screen_rect.right:
            self.x = self.screen_rect.right - self.rect.width
        if self.rect.top < 0:
            self.y = self.rect.height
        if self.rect.bottom > self.screen_rect.bottom:
            self.y = self.screen_rect.bottom - self.rect.height

        # Update rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # Draw the ship in its position
        self.screen.blit(self.image, self.rect)
