# Global Import
import pygame

# Local Imports
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    # class constructor | passes x, y, constant SHOT_RADIUS to Base class constructor
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    # overrides Base class draw method | draws the shot sprite to screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    # overrides Base class update method | updates shot sprite to move in straight line
    def update(self, dt):
        self.position += (self.velocity * dt)