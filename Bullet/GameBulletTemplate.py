import pygame


class GameBullet(pygame.sprite.Sprite):
    class_damage = None
    class_speed = None

    def __init__(self,
                 start_x_position,
                 start_y_position,
                 is_owner_player,
                 image_filename):
        super(GameBullet, self).__init__()
        self.image = pygame.image.load(image_filename)
        self.rect = self.image.get_rect()
        self.rect.centerx = start_x_position
        self.rect.centery = start_y_position
        self.damage = self.class_damage
        self.speed = self.class_speed
        if is_owner_player:
            self.speed *= -1

    def update(self):
        self.rect.centery += self.speed
        if self.rect.bottom <= 0 or self.rect.top >= 1080:
            self.kill()

    def reduce_damage(self, reduce):
        self.damage -= reduce
        if self.damage <= 0:
            self.damage = 0

    def get_damage(self):
        return self.damage

    def get_speed(self):
        return self.speed
