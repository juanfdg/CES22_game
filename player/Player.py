from models.Ship import Ship

from ui.TextBox import TextBox
from ui.LivesBar import LivesBar


class Player(Ship):
    #  General constants
    INITIAL_LIVES = 3
    MAX_LIVES = 5
    NAME_BOX_FONT_SIZE = 20
    SCORE_BOX_FONT_SIZE = 20

    def __init__(self, screen, x, y, number, initial_lives=INITIAL_LIVES):
        super().__init__(screen, x, y)
        self.initialx = x
        self.initialy = y

        self.lives = initial_lives
        self.score = 0
        self.number = number
        self.name = f"PLAYER{number}"
        self.screen = screen

        # Calculate position of text boxes and lives bar
        self.display_width_factor = screen.get_width() / 800
        self.display_height_factor = screen.get_height() / 640
        self.NAME_BOX_CENTER = (self.display_width_factor * 100, self.display_height_factor * 25)
        self.SCORE_BOX_CENTER = (self.NAME_BOX_CENTER[0], self.NAME_BOX_CENTER[1] + 25)
        self.LIVES_BAR_CENTER = (self.SCORE_BOX_CENTER[0], self.SCORE_BOX_CENTER[1] + 30)

        # Create text boxes and lives bar
        self.name_box = TextBox(self.screen, self.NAME_BOX_CENTER, self.NAME_BOX_FONT_SIZE, self.name)
        self.score_box = TextBox(self.screen, self.SCORE_BOX_CENTER, self.SCORE_BOX_FONT_SIZE, f"{self.score}")
        self.lives_bar = LivesBar(self.LIVES_BAR_CENTER, self.lives)

    def add_score(self, points):
        self.score += points

    def update(self, event=None):
        # Change the score displayed
        self.score_box.set_dialogue(f"{self.score}")

        super().update()

    # Render the text boxes and lives bar
    def render(self):
        self.name_box.render()
        self.score_box.render()
        self.lives_bar.render(self.screen)

    # Eliminates the player from the current groups
    def kill(self):
        super().kill()
        self.lives -= 1

        # If lives are reduced to zero, player permanently dies
        if self.lives == 0:
            self.lives_bar.set_lives(self.lives)

