class Settings():
    """ store << alien invasion>> all settings"""

    def __init__(self) -> None:
        "init game settings"
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5

        # 子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        # 在 Python 中，元组的括号可以省略
        self.bullet_color = 60, 60, 60
