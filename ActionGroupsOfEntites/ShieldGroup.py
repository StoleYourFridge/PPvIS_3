import pygame
from ActionEntities.ActionEntities import ShieldBoxEntity


class ShieldGroup(pygame.sprite.Group):
    first_shift = 12.5
    second_shift = 37.5

    def __init__(self,
                 start_x_position,
                 start_y_position):
        super(ShieldGroup, self).__init__()
        self.add(ShieldBoxEntity(start_x_position - self.second_shift,
                                 start_y_position - self.second_shift))
        self.add(ShieldBoxEntity(start_x_position - self.first_shift,
                                 start_y_position - self.second_shift))
        self.add(ShieldBoxEntity(start_x_position + self.first_shift,
                                 start_y_position - self.second_shift))
        self.add(ShieldBoxEntity(start_x_position + self.second_shift,
                                 start_y_position - self.second_shift))
        self.add(ShieldBoxEntity(start_x_position - self.second_shift,
                                 start_y_position - self.first_shift))
        self.add(ShieldBoxEntity(start_x_position - self.first_shift,
                                 start_y_position - self.first_shift))
        self.add(ShieldBoxEntity(start_x_position + self.first_shift,
                                 start_y_position - self.first_shift))
        self.add(ShieldBoxEntity(start_x_position + self.second_shift,
                                 start_y_position - self.first_shift))
        self.add(ShieldBoxEntity(start_x_position - self.second_shift,
                                 start_y_position + self.first_shift))
        self.add(ShieldBoxEntity(start_x_position + self.second_shift,
                                 start_y_position + self.first_shift))
        self.add(ShieldBoxEntity(start_x_position - self.second_shift,
                                 start_y_position + self.second_shift))
        self.add(ShieldBoxEntity(start_x_position + self.second_shift,
                                 start_y_position + self.second_shift))
