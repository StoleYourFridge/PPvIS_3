from Bullet.GameBulletTemplate import GameBulletTemplate
import json


with open("BulletsData.json", "r") as f:
    class_data = json.load(f)


class ConstPowerHighSpeedBullet(GameBulletTemplate):
    class_damage = class_data["ConstPowerHighSpeedBullet"]["damage"]
    class_speed = class_data["ConstPowerHighSpeedBullet"]["speed"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 is_owner_player):
        super(ConstPowerHighSpeedBullet, self).__init__(start_x_position,
                                                        start_y_position,
                                                        is_owner_player,
                                                        "BulletAssets/something.jpg")


class ConstPowerMediumSpeedBullet(GameBulletTemplate):
    class_damage = class_data["ConstPowerMediumSpeedBullet"]["damage"]
    class_speed = class_data["ConstPowerMediumSpeedBullet"]["speed"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 is_owner_player):
        super(ConstPowerMediumSpeedBullet, self).__init__(start_x_position,
                                                          start_y_position,
                                                          is_owner_player,
                                                          "BulletAssets/something.jpg")


class VariatePowerLowSpeedBullet(GameBulletTemplate):
    class_damage = class_data["VariatePowerLowSpeedBullet"]["damage"]
    class_speed = class_data["VariatePowerLowSpeedBullet"]["speed"]
    border_step = class_data["VariatePowerLowSpeedBullet"]["border step"]
    reduce_damage_step = class_data["VariatePowerLowSpeedBullet"]["reduce damage step"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 is_owner_player):
        super(VariatePowerLowSpeedBullet, self).__init__(start_x_position,
                                                         start_y_position,
                                                         is_owner_player,
                                                         "BulletAssets/something.jpg")
        self.passed_distance = 0
        self.next_border = VariatePowerLowSpeedBullet.border_step

    def update(self):
        super(VariatePowerLowSpeedBullet, self).update()
        self.passed_distance += abs(self.speed)
        if self.passed_distance >= self.next_border:
            self.next_border += VariatePowerLowSpeedBullet.border_step
            self.reduce_damage(VariatePowerLowSpeedBullet.reduce_damage_step)
