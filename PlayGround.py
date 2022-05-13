import sys
import pygame
import json
from ActionEntities.ActionEntities import PlayerEntity, MysteryShipEntity, DetectionZone
from ActionGroupsOfEntites.ShieldGroup import ShieldGroup
from ActionGroupsOfEntites.EnemyGroup import EnemyGroup


with open("Config/ScreenSettingsData.json", "r") as f:
    SCREEN_SETTINGS = json.load(f)
WIDTH = SCREEN_SETTINGS["width"]
HEIGHT = SCREEN_SETTINGS["height"]
FPS = SCREEN_SETTINGS["fps"]
BLACK = (0, 0, 0)
PLAYER_DEFAULT_POSITION = [WIDTH / 2, HEIGHT - 50]
ENEMIES_DEFAULT_POSITION = [WIDTH - 50, HEIGHT / 2]
MYSTERY_DEFAULT_POSITION = [WIDTH, 30]
SHIELD_DEFAULT_POSITIONS = [[WIDTH/5, HEIGHT - 170],
                            [2 * WIDTH/5, HEIGHT - 170],
                            [3 * WIDTH/5, HEIGHT - 170],
                            [4 * WIDTH/5, HEIGHT - 170]]
with open("Config/EnemyWaveData.json", "r") as f:
    ENEMIES_WAVE_DATA = json.load(f)


class PlayGround:
    default_frames_to_update_enemies_position = 30
    default_frames_enemies_to_shoot = 35
    default_frames_to_mystery = 600

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.current_enemies_wave = 0
        self.frames_to_update_enemies_position = PlayGround.default_frames_to_update_enemies_position
        self.frames_enemies_to_shoot = PlayGround.default_frames_enemies_to_shoot
        self.points = 0
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.player = PlayerEntity(PLAYER_DEFAULT_POSITION[0],
                                   PLAYER_DEFAULT_POSITION[1],
                                   self.player_bullets)
        self.enemies = EnemyGroup(self.enemy_bullets,
                                  ENEMIES_DEFAULT_POSITION[0],
                                  ENEMIES_DEFAULT_POSITION[1],
                                  ENEMIES_WAVE_DATA[self.current_enemies_wave])
        self.mystery = pygame.sprite.GroupSingle()
        self.shields = [ShieldGroup(shield[0], shield[1]) for shield in SHIELD_DEFAULT_POSITIONS]
        self.detection_zone = DetectionZone()
        self.clock = pygame.time.Clock()

    def restart_game(self):
        self.points = 0
        self.current_enemies_wave = 0
        self.player_bullets.empty()
        self.enemy_bullets.empty()
        self.frames_to_update_enemies_position = PlayGround.default_frames_to_update_enemies_position
        self.frames_enemies_to_shoot = PlayGround.default_frames_enemies_to_shoot
        self.player.repair(PLAYER_DEFAULT_POSITION[0],
                           PLAYER_DEFAULT_POSITION[1])
        self.enemies.apply_enemy_entities(self.enemy_bullets,
                                          ENEMIES_DEFAULT_POSITION[0],
                                          ENEMIES_DEFAULT_POSITION[1],
                                          ENEMIES_WAVE_DATA[self.current_enemies_wave])
        for shield in self.shields:
            shield.empty()
        self.shields.clear()
        self.shields = [ShieldGroup(shield[0], shield[1]) for shield in SHIELD_DEFAULT_POSITIONS]

    @staticmethod
    def deal_with_group_bullet_collision(group,
                                         group_of_bullets):
        price_collected = 0
        collision = pygame.sprite.groupcollide(group,
                                               group_of_bullets,
                                               False,
                                               True)
        for instance, bullets_passed_in_it in collision.items():
            for bullet in bullets_passed_in_it:
                instance.reduce_health(bullet.get_damage())
            if instance.get_health() <= 0:
                price_collected += instance.get_price()
        return price_collected

    def deal_with_shield_bullet_collision(self,
                                          group_of_bullets):
        for shield in self.shields:
            PlayGround.deal_with_group_bullet_collision(shield,
                                                        group_of_bullets)

    def deal_with_shield_enemy_collision(self):
        for shield in self.shields:
            pygame.sprite.groupcollide(shield,
                                       self.enemies,
                                       True,
                                       False,
                                       pygame.sprite.collide_circle)

    def deal_with_player_bullet_collision(self):
        collision = pygame.sprite.spritecollide(self.player,
                                                self.enemy_bullets,
                                                True)
        for bullet in collision:
            self.player.reduce_health(bullet.get_damage())

    def deal_with_enemy_bullet_collision(self):
        return PlayGround.deal_with_group_bullet_collision(self.enemies,
                                                           self.player_bullets)

    def deal_with_mystery_bullet_collision(self):
        return PlayGround.deal_with_group_bullet_collision(self.mystery,
                                                           self.player_bullets)

    def deal_with_bullet_bullet_collision(self):
        pygame.sprite.groupcollide(self.player_bullets,
                                   self.enemy_bullets,
                                   True,
                                   True)

    def deal_with_enemy_detection_zone_collision(self):
        if pygame.sprite.spritecollide(self.detection_zone,
                                       self.enemies,
                                       False):
            return True
        return False

    def collision_controller(self):
        self.deal_with_shield_bullet_collision(self.player_bullets)
        self.deal_with_shield_bullet_collision(self.enemy_bullets)
        self.deal_with_shield_enemy_collision()
        self.deal_with_player_bullet_collision()
        self.points += self.deal_with_enemy_bullet_collision()
        self.points += self.deal_with_mystery_bullet_collision()
        self.deal_with_bullet_bullet_collision()

    def mystery_except(self):
        self.mystery.add(MysteryShipEntity(MYSTERY_DEFAULT_POSITION[0],
                                           MYSTERY_DEFAULT_POSITION[1]))

    def win_checker(self):
        if len(self.enemies) == 0:
            return True
        return False

    def defeat_checker(self):
        if self.player.get_health() <= 0 or self.deal_with_enemy_detection_zone_collision():
            return True
        return False

    def increase_difficulty_level(self):
        self.frames_to_update_enemies_position -= 10
        self.frames_enemies_to_shoot -= 5

    def level_changer(self):
        self.enemy_bullets.empty()
        self.player_bullets.empty()
        pygame.time.wait(1000)
        self.player.increase_health(1)
        self.current_enemies_wave += 1
        if self.current_enemies_wave == len(ENEMIES_WAVE_DATA):
            self.current_enemies_wave = 0
            self.increase_difficulty_level()
        self.enemies.apply_enemy_entities(self.enemy_bullets,
                                          ENEMIES_DEFAULT_POSITION[0],
                                          ENEMIES_DEFAULT_POSITION[1],
                                          ENEMIES_WAVE_DATA[self.current_enemies_wave])
        pygame.time.wait(1000)

    def screen_entities_update(self):
        self.player.update()
        self.player_bullets.update()
        self.enemy_bullets.update()
        self.mystery.update()

    def screen_entities_draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.player.image,
                         self.player.rect)
        self.enemies.draw(self.screen)
        self.mystery.draw(self.screen)
        for shield in self.shields:
            shield.draw(self.screen)
        self.player_bullets.draw(self.screen)
        self.enemy_bullets.draw(self.screen)

    def run(self):
        pygame.init()
        frames_to_move = 0
        frames_to_shoot = 0
        frames_to_mystery = 0
        while True:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen_entities_update()
            if frames_to_shoot == self.frames_enemies_to_shoot:
                self.enemies.shoot()
                frames_to_shoot = 0
            if frames_to_move == self.frames_to_update_enemies_position:
                self.enemies.update()
                frames_to_move = 0
            if frames_to_mystery == self.default_frames_to_mystery:
                self.mystery_except()
                frames_to_mystery = 0
            self.collision_controller()

            self.screen_entities_draw()
            pygame.display.update()

            if self.win_checker():
                self.level_changer()
            if self.defeat_checker():
                break

            frames_to_move += 1
            frames_to_shoot += 1
            frames_to_mystery += 1


PlayGround = PlayGround()
PlayGround.run()
