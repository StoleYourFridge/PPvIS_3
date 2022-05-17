import pygame
import json


pygame.init()
with open("Config/ScreenSettingsData.json", "r") as f:
    SCREEN_SETTINGS = json.load(f)
WIDTH = SCREEN_SETTINGS["width"]
HEIGHT = SCREEN_SETTINGS["height"]
SCREEN_BACKGROUND_COLOR = [0, 0, 0]
FPS = SCREEN_SETTINGS["fps"]
TEXT_FONT = pygame.font.SysFont("arial", 30)
TEXT_COLOR = [255, 255, 255]


class GameRules:
    def __init__(self,
                 screen_manager):
        self.screen_manager = screen_manager
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.entities_data = {}
        self.set_entities_data()
        self.clock = pygame.time.Clock()

    @staticmethod
    def entity_data(health,
                    price,
                    weapon_preset):
        return "health: {0}    price: {1}    weapon preset: {2}".format(str(health),
                                                                        str(price),
                                                                        str(weapon_preset))

    def set_entities_data(self):
        with open("Config/ActionEntitiesData.json") as f:
            self.entities_data = json.load(f)

    def draw_entity_data(self,
                         name_text,
                         image_filename,
                         health,
                         price,
                         weapon_preset,
                         start_y_position):
        name = TEXT_FONT.render(name_text,
                                True,
                                TEXT_COLOR)
        image = pygame.image.load(image_filename)
        data = TEXT_FONT.render(GameRules.entity_data(health,
                                                      price,
                                                      weapon_preset),
                                True,
                                TEXT_COLOR)
        self.screen.blit(name,
                         (100, start_y_position))
        self.screen.blit(image,
                         (300, start_y_position))
        self.screen.blit(data,
                         (400, start_y_position))

    def draw_elements(self):
        self.screen.fill(SCREEN_BACKGROUND_COLOR)
        self.screen.blit(TEXT_FONT.render("MAIN ENTITIES",
                                          True,
                                          TEXT_COLOR),
                         (WIDTH / 2 - 40, 20))
        self.draw_entity_data("Player",
                              "ActionEntities/ActionEntitiesAssets/Player/Player.png",
                              self.entities_data["PlayerEntity"]["health"],
                              0,
                              "1-3",
                              100)
        self.draw_entity_data("ShieldBox",
                              "ActionEntities/ActionEntitiesAssets/ShieldBox/State_1.png",
                              self.entities_data["ShieldBoxEntity"]["health"],
                              0,
                              "None",
                              200)
        self.draw_entity_data("Mystery",
                              "ActionEntities/ActionEntitiesAssets/MysteryShip/AliveState.png",
                              self.entities_data["MysteryShipEntity"]["health"],
                              self.entities_data["MysteryShipEntity"]["price"],
                              "None",
                              300)
        self.draw_entity_data("Enemy",
                              "ActionEntities/ActionEntitiesAssets/Enemy/LevelOneEnemy.png",
                              "1 - 4",
                              "10 - 150",
                              "1 - 3",
                              400)
        self.screen.blit(TEXT_FONT.render("Main Goal: preventing enemies to invade players base al long as you can.",
                                          True,
                                          TEXT_COLOR),
                         (WIDTH / 2 - 400, 500))

    def run(self):
        self.draw_elements()
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.screen_manager.next_action = "Exit"
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.screen_manager.next_action = "Menu"
                        return
            pygame.display.flip()
