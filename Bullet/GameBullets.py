from Bullet.GameBulletTemplate import GameBullet
import json


with open("BulletsData.json", "r") as f:
    class_data = json.load(f)


class ConstPowerHighSpeedBullet(GameBullet):
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
