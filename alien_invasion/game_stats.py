class Gamestats():
    """跟踪游戏统计信息"""
    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """初始化统计信息"""
        self.ship_left  = self.ai_settings.ship_limit
        self.game_active = True