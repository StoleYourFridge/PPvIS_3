import pygame
from random import randrange
from ActionEntities.ActionEntities import LevelOneEnemy, LevelTwoEnemy, LevelThreeEnemy, LevelFourEnemy, LevelFiveEnemy
from ActionEntities.ActionEntities import LevelSixEnemy, LevelSevenEnemy, LevelEightEnemy, LevelNineEnemy, LevelTenEnemy
from ActionEntities.ActionEntities import LevelElevenEnemy, LevelTwelveEnemy


class EnemyGroup(pygame.sprite.Group):
    cols_length = 50
    rows_length = 50
    entities_in_one_row = 11
    horizontal_step = 20
    vertical_step = 20

    def __init__(self,
                 group_of_bullets,
                 root_x_position,
                 root_y_position,
                 enemy_entity_names):
        super(EnemyGroup, self).__init__()
        self.x_step = -EnemyGroup.horizontal_step
        self.y_step = 0
        self.direction = "left"
        self.dropped = False
        self.apply_enemy_entities(group_of_bullets,
                                  root_x_position,
                                  root_y_position,
                                  enemy_entity_names)

    def get_x_step(self):
        return self.x_step

    def get_y_step(self):
        return self.y_step

    def apply_enemy_entities(self,
                             group_of_bullets,
                             root_x_position,
                             root_y_position,
                             enemy_entity_names):
        self.empty()
        current_x_position = root_x_position
        for entity in enemy_entity_names:
            for number in range(EnemyGroup.entities_in_one_row):
                if entity == "LevelOneEnemy":
                    self.add(LevelOneEnemy(current_x_position,
                                           root_y_position,
                                           group_of_bullets))
                elif entity == "LevelTwoEnemy":
                    self.add(LevelTwoEnemy(current_x_position,
                                           root_y_position,
                                           group_of_bullets))
                elif entity == "LevelThreeEnemy":
                    self.add(LevelThreeEnemy(current_x_position,
                                             root_y_position,
                                             group_of_bullets))
                elif entity == "LevelFourEnemy":
                    self.add(LevelFourEnemy(current_x_position,
                                            root_y_position,
                                            group_of_bullets))
                elif entity == "LevelFiveEnemy":
                    self.add(LevelFiveEnemy(current_x_position,
                                            root_y_position,
                                            group_of_bullets))
                elif entity == "LevelSixEnemy":
                    self.add(LevelSixEnemy(current_x_position,
                                           root_y_position,
                                           group_of_bullets))
                elif entity == "LevelSevenEnemy":
                    self.add(LevelSevenEnemy(current_x_position,
                                             root_y_position,
                                             group_of_bullets))
                elif entity == "LevelEightEnemy":
                    self.add(LevelEightEnemy(current_x_position,
                                             root_y_position,
                                             group_of_bullets))
                elif entity == "LevelNineEnemy":
                    self.add(LevelNineEnemy(current_x_position,
                                            root_y_position,
                                            group_of_bullets))
                elif entity == "LevelTenEnemy":
                    self.add(LevelTenEnemy(current_x_position,
                                           root_y_position,
                                           group_of_bullets))
                elif entity == "LevelElevenEnemy":
                    self.add(LevelElevenEnemy(current_x_position,
                                              root_y_position,
                                              group_of_bullets))
                elif entity == "LevelTwelveEnemy":
                    self.add(LevelTwelveEnemy(current_x_position,
                                              root_y_position,
                                              group_of_bullets))
                current_x_position -= EnemyGroup.cols_length
            current_x_position = root_x_position
            root_y_position -= EnemyGroup.rows_length

    def shoot(self):
        sprites = self.sprites()
        sprites[randrange(0, len(self), 1)].shoot()

    def change_sprites_horizontal_direction(self):
        if self.direction == "left":
            self.direction = "right"
            self.x_step = EnemyGroup.horizontal_step
        elif self.direction == "right":
            self.direction = "left"
            self.x_step = -EnemyGroup.horizontal_step

    def refresh_predicted_sprites_step(self):
        sprites_position_status = set()
        for sprite in self.sprites():
            sprites_position_status.add(sprite.get_position_status())
        if True in sprites_position_status and not self.dropped:
            self.dropped = True
            self.x_step = 0
            self.y_step = EnemyGroup.vertical_step
            return
        if self.dropped:
            self.dropped = False
            self.y_step = 0
            self.change_sprites_horizontal_direction()

    def update(self):
        super(EnemyGroup, self).update(self.x_step, self.y_step)
        self.refresh_predicted_sprites_step()
