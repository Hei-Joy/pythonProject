import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化飞机， 并设置起始位置"""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞机图像并获取其外界矩形
        self.image = pygame.image.load('images/life.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每一艘新飞机放在屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞机的数学center中存储小数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """"根据移动位置调整飞机位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center跟新rectd对象
        self.rect.centerx = self.center

    def blitem(self):
        # 指定位置绘制飞机
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞机在屏幕上居中"""
        self.center = self.screen_rect.centerx
