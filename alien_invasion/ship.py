import pygame

class Ship():
    # 飞船类
    def __init__(self,ai_settings,screen):
        """初始化飞船 设置飞船位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取外接矩阵
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #每只出现的飞船放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #center中存储小数
        self.center = float(self.rect.centerx)
        self.center1 = float(self.rect.centery)

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_dowm = False

    def update(self):
        """根据标志移动飞船"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:
            self.center1 -= self.ai_settings.ship_speed_factor
        if self.moving_dowm and self.rect.bottom < self.screen_rect.bottom:
            self.center1 += self.ai_settings.ship_speed_factor
        # 根据center修改rect
        self.rect.centerx = self.center
        self.rect.centery = self.center1
    def blitme(self):
        """指定位置显示飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom