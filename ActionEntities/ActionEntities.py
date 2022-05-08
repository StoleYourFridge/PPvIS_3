from ActionEntityTemplates import ActionEntityTemplate, EnemyEntityTemplate, ShootingAbilityEntity
import json
import pygame


with open("ActionEntitiesData.json", "r") as f:
    class_data = json.load(f)


class PlayerEntity(ShootingAbilityEntity):
    class_health = class_data["PlayerEntity"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(PlayerEntity, self).__init__(start_x_position,
                                           start_y_position,
                                           class_data["PlayerEntity"]["default bullet preset"],
                                           group_of_bullets,
                                           class_data["PlayerEntity"]["reload change index"],
                                           "ActionEntitiesAssets/Player/something.jpg")
        self.speed = class_data["PlayerEntity"]["speed"]

    def move(self, parameter):
        if parameter == "right":
            self.rect.centerx += self.speed
        elif parameter == "left":
            self.rect.centerx -= self.speed

    def get_conflict_side(self):
        return True

    def kill_action(self):
        self.kill()


class MysteryShipEntity(ActionEntityTemplate):
    class_health = class_data["MysteryShipEntity"]["health"]
    frames_to_be_killed = 10

    def __init__(self,
                 start_x_position,
                 start_y_position):
        super(MysteryShipEntity, self).__init__(start_x_position,
                                                start_y_position,
                                                "ActionEntitiesAssets/MysteryShip/AliveState.jpg")
        self.price = class_data["MysteryShipEntity"]["price"]
        self.speed = class_data["MysteryShipEntity"]["speed"]
        self.frames_to_be_killed = self.frames_to_be_killed
        self.frames_after_killing = 0
        self.killed = False

    def kill_action(self):
        self.killed = True
        self.image = pygame.image.load("ActionEntitiesAssets/MysteryShip/KillState.jpg")

    def update(self):
        self.rect.centerx += self.speed
        if self.killed:
            self.frames_after_killing += 1
        if self.frames_after_killing == self.frames_to_be_killed:
            self.kill()


class ShieldBoxEntity(ActionEntityTemplate):
    class_health = class_data["ShieldBoxEntity"]["health"]
    killing_states = [pygame.image.load("ActionEntitiesAssets/ShieldBox/State_{}.jpg".format(i + 1)) for i in
                      range(class_health)]

    def __init__(self,
                 start_x_position,
                 start_y_position):
        super(ShieldBoxEntity, self).__init__(start_x_position,
                                              start_y_position,
                                              "ActionEntitiesAssets/ShieldBox/State_1.jpg")
        self.killing_state = 0

    def correct_killing_state(self):
        if self.health <= 3:
            self.killing_state = 1
        elif self.health <= 2:
            self.killing_state = 2
        elif self.health <= 1:
            self.killing_state = 3

    def reduce_health(self, reduce):
        super(ShieldBoxEntity, self).reduce_health(reduce)
        self.correct_killing_state()
        self.image = ShieldBoxEntity.killing_states[self.killing_state]

    def kill_action(self):
        self.kill()


class LevelOneEnemy(EnemyEntityTemplate):
    class_price = class_data["LevelOneEnemy"]["price"]
    class_health = class_data["LevelOneEnemy"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(LevelOneEnemy, self).__init__(start_x_position,
                                            start_y_position,
                                            class_data["LevelOneEnemy"]["default bullet preset"],
                                            group_of_bullets,
                                            class_data["LevelOneEnemy"]["reload change index"],
                                            "ActionEntitiesAssets/Enemy/LevelOneEnemy.jpg")


class LevelTwoEnemy(EnemyEntityTemplate):
    class_price = class_data["LevelTwoEnemy"]["price"]
    class_health = class_data["LevelTwoEnemy"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(LevelTwoEnemy, self).__init__(start_x_position,
                                            start_y_position,
                                            class_data["LevelTwoEnemy"]["default bullet preset"],
                                            group_of_bullets,
                                            class_data["LevelTwoEnemy"]["reload change index"],
                                            "ActionEntitiesAssets/Enemy/LevelTwoEnemy.jpg")


class LevelThreeEnemy(EnemyEntityTemplate):
    class_price = class_data["LevelThreeEnemy"]["price"]
    class_health = class_data["LevelThreeEnemy"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(LevelThreeEnemy, self).__init__(start_x_position,
                                              start_y_position,
                                              class_data["LevelThreeEnemy"]["default bullet preset"],
                                              group_of_bullets,
                                              class_data["LevelThreeEnemy"]["reload change index"],
                                              "ActionEntitiesAssets/Enemy/LevelThreeEnemy.jpg")


class LevelFourEnemy(EnemyEntityTemplate):
    class_price = class_data["LevelFourEnemy"]["price"]
    class_health = class_data["LevelFourEnemy"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(LevelFourEnemy, self).__init__(start_x_position,
                                             start_y_position,
                                             class_data["LevelFourEnemy"]["default bullet preset"],
                                             group_of_bullets,
                                             class_data["LevelFourEnemy"]["reload change index"],
                                             "ActionEntitiesAssets/Enemy/LevelFourEnemy.jpg")


class LevelFiveEnemy(EnemyEntityTemplate):
    class_price = class_data["LevelFiveEnemy"]["price"]
    class_health = class_data["LevelFiveEnemy"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(LevelFiveEnemy, self).__init__(start_x_position,
                                             start_y_position,
                                             class_data["LevelFiveEnemy"]["default bullet preset"],
                                             group_of_bullets,
                                             class_data["LevelFiveEnemy"]["reload change index"],
                                             "ActionEntitiesAssets/Enemy/LevelFiveEnemy.jpg")


class LevelSixEnemy(EnemyEntityTemplate):
    class_price = class_data["LevelSixEnemy"]["price"]
    class_health = class_data["LevelSixEnemy"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(LevelSixEnemy, self).__init__(start_x_position,
                                            start_y_position,
                                            class_data["LevelSixEnemy"]["default bullet preset"],
                                            group_of_bullets,
                                            class_data["LevelSixEnemy"]["reload change index"],
                                            "ActionEntitiesAssets/Enemy/LevelSixEnemy.jpg")


class LevelSevenEnemy(EnemyEntityTemplate):
    class_price = class_data["LevelSevenEnemy"]["price"]
    class_health = class_data["LevelSevenEnemy"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(LevelSevenEnemy, self).__init__(start_x_position,
                                              start_y_position,
                                              class_data["LevelSevenEnemy"]["default bullet preset"],
                                              group_of_bullets,
                                              class_data["LevelSevenEnemy"]["reload change index"],
                                              "ActionEntitiesAssets/Enemy/LevelSevenEnemy.jpg")


class LevelEightEnemy(EnemyEntityTemplate):
    class_price = class_data["LevelEightEnemy"]["price"]
    class_health = class_data["LevelEightEnemy"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(LevelEightEnemy, self).__init__(start_x_position,
                                              start_y_position,
                                              class_data["LevelEightEnemy"]["default bullet preset"],
                                              group_of_bullets,
                                              class_data["LevelEightEnemy"]["reload change index"],
                                              "ActionEntitiesAssets/Enemy/LevelEightEnemy.jpg")


class LevelNineEnemy(EnemyEntityTemplate):
    class_price = class_data["LevelNineEnemy"]["price"]
    class_health = class_data["LevelNineEnemy"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(LevelNineEnemy, self).__init__(start_x_position,
                                             start_y_position,
                                             class_data["LevelNineEnemy"]["default bullet preset"],
                                             group_of_bullets,
                                             class_data["LevelNineEnemy"]["reload change index"],
                                             "ActionEntitiesAssets/Enemy/LevelNineEnemy.jpg")


class LevelTenEnemy(EnemyEntityTemplate):
    class_price = class_data["LevelTenEnemy"]["price"]
    class_health = class_data["LevelTenEnemy"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(LevelTenEnemy, self).__init__(start_x_position,
                                            start_y_position,
                                            class_data["LevelTenEnemy"]["default bullet preset"],
                                            group_of_bullets,
                                            class_data["LevelTenEnemy"]["reload change index"],
                                            "ActionEntitiesAssets/Enemy/LevelTenEnemy.jpg")


class LevelElevenEnemy(EnemyEntityTemplate):
    class_price = class_data["LevelElevenEnemy"]["price"]
    class_health = class_data["LevelElevenEnemy"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(LevelElevenEnemy, self).__init__(start_x_position,
                                               start_y_position,
                                               class_data["LevelElevenEnemy"]["default bullet preset"],
                                               group_of_bullets,
                                               class_data["LevelElevenEnemy"]["reload change index"],
                                               "ActionEntitiesAssets/Enemy/LevelElevenEnemy.jpg")


class LevelTwelveEnemy(EnemyEntityTemplate):
    class_price = class_data["LevelTwelveEnemy"]["price"]
    class_health = class_data["LevelTwelveEnemy"]["health"]

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 group_of_bullets):
        super(LevelTwelveEnemy, self).__init__(start_x_position,
                                               start_y_position,
                                               class_data["LevelTwelveEnemy"]["default bullet preset"],
                                               group_of_bullets,
                                               class_data["LevelTwelveEnemy"]["reload change index"],
                                               "ActionEntitiesAssets/Enemy/LevelTwelveEnemy.jpg")
