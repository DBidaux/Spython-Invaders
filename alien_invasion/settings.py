# Class to save all settings

class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_rotation_speed = 0.25
        self.ship_limit = 5

        # Bullet settings

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (87, 168, 255)
        self.bullets_allowed = 3

        # Alien settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        self.ship_speed = 0.75
        self.bullet_speed = 2
        self.alien_speed = 0.5
        self.fleet_direction = 0.6
        self.fleet_drop_speed = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def set_difficult(self, difficult):
        if difficult == "easy":
            self.ship_speed = 0.75
            self.bullet_speed = 2
            self.alien_speed = 0.5
            self.fleet_drop_speed = 1.5
        if difficult == "medium":
            self.ship_speed = 1
            self.bullet_speed = 3
            self.alien_speed = 0.75
            self.fleet_drop_speed = 2
        if difficult == "hard":
            self.ship_speed = 1.5
            self.bullet_speed = 4
            self.alien_speed = 1
            self.fleet_drop_speed = 2.5
