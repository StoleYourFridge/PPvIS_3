from GameScreens.PlayGround import PlayGround
from GameScreens.Menu import Menu
from GameScreens.Records import Records
from GameScreens.GameRules import GameRules
from pygame import mixer
mixer.music.load("GameScreens/MenuSound/MenuMusic.mp3")
mixer.music.set_volume(0.2)


class ScreenManager:
    def __init__(self):
        self.playground = PlayGround(self)
        self.menu = Menu(self)
        self.records = Records(self)
        self.game_rules = GameRules(self)
        self.next_action = "Menu"

    def run(self):
        mixer.music.play(-1)
        while True:
            if self.next_action == "PlayGround":
                mixer.music.stop()
                self.playground.restart_game()
                self.playground.run()
                mixer.music.play(-1)
            elif self.next_action == "Menu":
                self.menu.run()
            elif self.next_action == "Records":
                self.records.run()
            elif self.next_action == "GameRules":
                self.game_rules.run()
            elif self.next_action == "Exit":
                return
