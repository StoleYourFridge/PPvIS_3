import pygame
import json


pygame.init()
with open("Config/ScreenSettingsData.json", "r") as f:
    SCREEN_SETTINGS = json.load(f)
WIDTH = SCREEN_SETTINGS["width"]
HEIGHT = SCREEN_SETTINGS["height"]
SCREEN_BACKGROUND_COLOR = [0, 0, 0]
FPS = SCREEN_SETTINGS["fps"]
MENU_ELEMENT_SIZE = [400, 100]
MENU_ELEMENT_NAMES = ["Play", "Records", "Game Rules", "Exit"]
ACTIVE_BACKGROUND_COLOR = [255, 255, 255]
INACTIVE_BACKGROUND_COLOR = [50, 50, 0]
TEXT_FONT = pygame.font.SysFont("arial", 50)
TEXT_COLOR = [0, 0, 0]


class MenuElement(pygame.surface.Surface):
    def __init__(self,
                 element_text):
        super(MenuElement, self).__init__(MENU_ELEMENT_SIZE)
        self.text = TEXT_FONT.render(element_text,
                                     True,
                                     TEXT_COLOR)
        self.set_inactive()

    def set_active(self):
        self.fill(ACTIVE_BACKGROUND_COLOR)
        self.blit(self.text,
                  (100, 25))

    def set_inactive(self):
        self.fill(INACTIVE_BACKGROUND_COLOR)
        self.blit(self.text,
                  (100, 25))


class Menu:
    start_element_vertical_position = 100
    element_vertical_step = 150

    def __init__(self,
                 screen_manager):
        self.screen_manager = screen_manager
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.menu_elements = []
        self.current_active_menu_element = 0
        self.clock = pygame.time.Clock()
        self.set_menu_elements()

    def draw_menu_elements(self):
        vertical_position = Menu.start_element_vertical_position
        for menu_element in self.menu_elements:
            self.screen.blit(menu_element,
                             (WIDTH / 2 - 400 / 2,
                              vertical_position))
            vertical_position += Menu.element_vertical_step

    def set_menu_elements(self):
        for menu_element_name in MENU_ELEMENT_NAMES:
            self.menu_elements.append(MenuElement(menu_element_name))
        self.menu_elements[self.current_active_menu_element].set_active()

    def active_up(self):
        self.menu_elements[self.current_active_menu_element].set_inactive()
        self.current_active_menu_element -= 1
        if self.current_active_menu_element < 0:
            self.current_active_menu_element = len(self.menu_elements) - 1
        self.menu_elements[self.current_active_menu_element].set_active()
        self.draw_menu_elements()

    def active_down(self):
        self.menu_elements[self.current_active_menu_element].set_inactive()
        self.current_active_menu_element += 1
        if self.current_active_menu_element >= len(self.menu_elements):
            self.current_active_menu_element = 0
        self.menu_elements[self.current_active_menu_element].set_active()
        self.draw_menu_elements()

    def on_enter(self):
        if self.current_active_menu_element == 0:
            self.screen_manager.next_action = "PlayGround"
        elif self.current_active_menu_element == 1:
            self.screen_manager.next_action = "Records"
        elif self.current_active_menu_element == 2:
            self.screen_manager.next_action = "GameRules"
        elif self.current_active_menu_element == 3:
            self.screen_manager.next_action = "Exit"

    def run(self):
        self.screen.fill(SCREEN_BACKGROUND_COLOR)
        self.draw_menu_elements()
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.screen_manager.next_action = "Exit"
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.active_up()
                    elif event.key == pygame.K_DOWN:
                        self.active_down()
                    elif event.key == pygame.K_RETURN:
                        self.on_enter()
                        return
            pygame.display.flip()
