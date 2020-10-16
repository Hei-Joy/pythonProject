import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """对子弹管理类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞机所在位置创建子弹"""
        super().__init__()
        self.screen = screen

        # 创建一个0，0位置的子弹矩形，再将其设置为正确位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 用小数存储子弹位置
        self.y = float(ship.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        self.y -= self.speed_factor
        # 更新子弹的rect的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
