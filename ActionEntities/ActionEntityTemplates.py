import pygame
from Weapon.Weapon import Weapon


class ActionEntityTemplate(pygame.sprite.Sprite):
    class_health = None

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 image_filename):
        super(ActionEntityTemplate, self).__init__()
        self.image = pygame.image.load(image_filename)
        self.rect = self.image.get_rect()
        self.rect.centerx = start_x_position
        self.rect.centery = start_y_position
        self.health = self.class_health

    def kill_action(self):
        pass

    def reduce_health(self, reduce):
        self.health -= reduce
        if self.health <= 0:
            self.kill_action()


class ShootingAbilityEntity(ActionEntityTemplate):
    def __init__(self,
                 start_x_position,
                 start_y_position,
                 default_bullet_preset,
                 group_of_bullets,
                 reload_change_index,
                 image_filename):
        super(ShootingAbilityEntity, self).__init__(start_x_position,
                                                    start_y_position,
                                                    image_filename)
        self.weapon = Weapon(self,
                             default_bullet_preset,
                             reload_change_index)
        self.group_of_bullets = group_of_bullets

    def get_conflict_side(self):
        pass

    def shoot(self):
        self.weapon.shoot()

    def change_bullet_preset(self, preset):
        self.weapon.change_bullet_preset(preset)


class EnemyEntityTemplate(ShootingAbilityEntity):
    class_price = None
    frames_to_be_killed = 10

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 default_bullet_preset,
                 group_of_bullets,
                 reload_change_index,
                 image_filename):
        super(EnemyEntityTemplate, self).__init__(start_x_position,
                                                  start_y_position,
                                                  default_bullet_preset,
                                                  group_of_bullets,
                                                  reload_change_index,
                                                  image_filename)
        self.price = self.class_price
        self.frames_after_killing = 0
        self.killed = False

    def get_conflict_side(self):
        return False

    def get_price(self):
        return self.price

    def kill_action(self):
        self.killed = True
        self.image = pygame.image.load("ActionEntitiesAssets/Enemy/KillState.jpg")

    def update(self, x_shift, y_shift):
        self.rect.centerx += x_shift
        self.rect.centery += y_shift
        if self.killed:
            self.frames_after_killing += 1
        if self.frames_after_killing == self.frames_to_be_killed:
            self.kill()
