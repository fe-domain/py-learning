import pygame


class Ship():
    def __init__(self, ai_settings, screen) -> None:
        """ init spaceship and set its location"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its external matrix
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # place each new ship in the bottom center of the screen
        self.rect_centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        # 移动的标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志来调整飞船的位置"""
        # 更新飞船的 center 值，而不是 rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据 self.center 更新 rect 对象
        self.rect.centerx = self.center

    def blitme(self):
        """ draw the spaceship at the specified location """
        self.screen.blit(self.image, self.rect)
