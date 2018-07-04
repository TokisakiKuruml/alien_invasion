class Settings():
    """ 存储所有的设置属性的类"""
    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕设置属性
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #飞船属性
        self.ship_speed_factor = 1.2
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3


        # 外星人属性设置
        self.alien_speed_factor = 0.7
        self.fleet_drop_speed = 12
        self.fleet_direction = 1