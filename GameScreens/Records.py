import pygame
import json


pygame.init()
with open("Config/ScreenSettingsData.json", "r") as f:
    SCREEN_SETTINGS = json.load(f)
WIDTH = SCREEN_SETTINGS["width"]
HEIGHT = SCREEN_SETTINGS["height"]
SCREEN_BACKGROUND_COLOR = [0, 0, 0]
FPS = SCREEN_SETTINGS["fps"]
MAXIMUM_RECORDS = 8
RECORD_ELEMENT_SIZE = [600, 60]
RECORDS_ELEMENT_BACKGROUND_COLOR = [255, 255, 255]
TEXT_FONT = pygame.font.SysFont("arial", 40)
TEXT_COLOR = [0, 0, 0]


class RecordsElement(pygame.surface.Surface):
    def __init__(self,
                 name_text,
                 score_text):
        super(RecordsElement, self).__init__(RECORD_ELEMENT_SIZE)
        self.fill(RECORDS_ELEMENT_BACKGROUND_COLOR)
        name = TEXT_FONT.render(name_text,
                                True,
                                TEXT_COLOR)
        score = TEXT_FONT.render(score_text,
                                 True,
                                 TEXT_COLOR)
        self.blit(name,
                  (50, 10))
        self.blit(score,
                  (500, 10))


class Records:
    start_element_vertical_position = 20
    element_vertical_step = 90

    def __init__(self,
                 screen_manager):
        self.screen_manager = screen_manager
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.records_data = []
        self.clock = pygame.time.Clock()

    def set_records_data(self):
        with open("Config/RecordsData.json", "r") as f:
            self.records_data = json.load(f)

    def draw_records_elements(self):
        vertical_position = Records.start_element_vertical_position
        controller = 0
        self.set_records_data()
        self.screen.fill(SCREEN_BACKGROUND_COLOR)
        for record_data in self.records_data:
            record = RecordsElement(record_data["name"],
                                    str(record_data["score"]))
            self.screen.blit(record,
                             (WIDTH / 2 - 600 / 2,
                              vertical_position))
            vertical_position += Records.element_vertical_step
            controller += 1
            if controller == MAXIMUM_RECORDS:
                break

    def run(self):
        self.draw_records_elements()
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
