import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        # 初始化敌机并设置其起始位置
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # 加载敌机图像，并设置rect
        self.image = pygame.image.load('images/enemy1.png')
        self.rect = self.image.get_rect()

        # 将每一艘新敌机放在屏幕右上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 在存储敌机准确位置
        self.center = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitem(self):
        # 指定位置绘制敌机
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """如果敌机位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向右或向左移动敌机"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x