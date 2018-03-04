import pygame
from models.Asteroid import Asteroid


class SmallAsteroid(Asteroid):

    def __init__(self, screen, x=None, y=None, speed=None, vel_dir=None):
        super().__init__(screen, 0.09, x, y, speed, vel_dir)

    def destroy(self):
        self.kill()

        # TODO(Victor) Find a reasonable return. SEE tests/TestAsteroidsDestruction
        return None