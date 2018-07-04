import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """外星人类"""
    def __init__(self,ai_settings,screen):
        """创建外星人设置起始位置"""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        #加载图像获取rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #设置初始位置为左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #小数存储位置
        self.x = float(self.rect.x)

    def blitme(self):
        """指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """检测是否接触屏幕边界"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
