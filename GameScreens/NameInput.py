from pygame_functions import screenSize, makeTextBox, showTextBox, textBoxInput
import pygame
import json


with open("Config/ScreenSettingsData.json", "r") as f:
    SCREEN_SETTINGS = json.load(f)
WIDTH = SCREEN_SETTINGS["width"]
HEIGHT = SCREEN_SETTINGS["height"]
TEXT_FONT = pygame.font.SysFont("arial", 40)
TEXT_COLOR = [255, 255, 255]
CONGRATULATIONS_MESSAGE = "HIGHEST RECORD IS BROKEN!"
WORD_BOX_WIDTH = 300
MAX_TEXT_LENGTH = 20
FONT_TEXT_SIZE = 30


def name_input():
    screen = screenSize(WIDTH,
                        HEIGHT)
    screen.blit(TEXT_FONT.render(CONGRATULATIONS_MESSAGE,
                                 True,
                                 TEXT_COLOR),
                (WIDTH / 2 - 250,
                 HEIGHT / 2 - 100))
    name_input_element = makeTextBox(WIDTH / 2 - 180,
                                     HEIGHT / 2,
                                     WORD_BOX_WIDTH,
                                     0,
                                     "Enter Your Name:",
                                     MAX_TEXT_LENGTH,
                                     FONT_TEXT_SIZE)
    showTextBox(name_input_element)
    return textBoxInput(name_input_element)
