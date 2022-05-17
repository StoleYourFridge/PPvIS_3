from GameScreens.PlayGround import PlayGround
from GameScreens.Menu import Menu
from GameScreens.Records import Records
from GameScreens.GameRules import GameRules


class ScreenManager:
    def __init__(self):
        self.playground = PlayGround(self)
        self.menu = Menu(self)
        self.records = Records(self)
        self.game_rules = GameRules(self)
        self.next_action = "Menu"

    def run(self):
        while True:
            if self.next_action == "PlayGround":
                self.playground.restart_game()
                self.playground.run()
            elif self.next_action == "Menu":
                self.menu.run()
            elif self.next_action == "Records":
                self.records.run()
            elif self.next_action == "GameRules":
                self.game_rules.run()
            elif self.next_action == "Exit":
                return
