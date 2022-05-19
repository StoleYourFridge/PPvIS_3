from Bullet.GameBullets import ConstPowerHighSpeedBullet, ConstPowerMediumSpeedBullet, VariatePowerLowSpeedBullet
import pygame
import json
import os

pygame.init()
with open("Config/WeaponReloadData.json", "r") as f:
    class_data = json.load(f)
SOUNDS_DIR = "Bullet/BulletSounds/"


class Weapon:
    weapons_call_down = class_data[:]
    weapons_sounds = [pygame.mixer.Sound(SOUNDS_DIR + sound_filename)
                      for sound_filename in os.listdir(SOUNDS_DIR)]

    def __init__(self,
                 parent_entity,
                 default_bullet_preset,
                 reload_change_index):
        self.parent_entity = parent_entity
        self.current_bullet_preset = default_bullet_preset
        self.reload_change_index = reload_change_index
        self.current_weapon_call_down = Weapon.weapons_call_down[default_bullet_preset - 1] * self.reload_change_index
        self.shoot_ability = True
        self.shoot_ability_timer = 0
        self.shoot_ability_clock = pygame.time.Clock()

    def correct_shoot_ability(self):
        self.shoot_ability_clock.tick()
        if not self.shoot_ability:
            self.shoot_ability_timer += self.shoot_ability_clock.get_time()
            if self.shoot_ability_timer >= self.current_weapon_call_down:
                self.shoot_ability = True
                self.shoot_ability_timer = 0

    def shoot_action(self):
        if self.current_bullet_preset == 1:
            self.parent_entity.group_of_bullets.add(ConstPowerHighSpeedBullet(self.parent_entity.rect.centerx,
                                                                              self.parent_entity.rect.centery,
                                                                              self.parent_entity.get_conflict_side()))
        if self.current_bullet_preset == 2:
            self.parent_entity.group_of_bullets.add(ConstPowerMediumSpeedBullet(self.parent_entity.rect.centerx,
                                                                                self.parent_entity.rect.centery,
                                                                                self.parent_entity.get_conflict_side()))
        if self.current_bullet_preset == 3:
            self.parent_entity.group_of_bullets.add(VariatePowerLowSpeedBullet(self.parent_entity.rect.centerx,
                                                                               self.parent_entity.rect.centery,
                                                                               self.parent_entity.get_conflict_side()))
        Weapon.weapons_sounds[self.current_bullet_preset - 1].play()

    def shoot(self):
        self.correct_shoot_ability()
        if not self.shoot_ability:
            return
        self.shoot_ability = False
        self.shoot_action()

    def change_bullet_preset(self, preset):
        self.current_bullet_preset = preset
        self.current_weapon_call_down = Weapon.weapons_call_down[self.current_bullet_preset - 1] * self.reload_change_index
        self.shoot_ability_clock.tick()
        self.shoot_ability_timer = 0
