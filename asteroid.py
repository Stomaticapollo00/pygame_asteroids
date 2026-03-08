# Global Import
import pygame

# Local Imports
from circleshape import CircleShape
from constants import LINE_WIDTH

# Asteroid Class inherit Base Class for Player object
class Asteroid(CircleShape):
    # class constructor | passes x, y, radius to Base class constructor
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # overrides Base class draw method | draws the asteroid sprite to screen
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    # overrides Base class update method | updates asteroid sprite to move in straight line
    def update(self, dt):
        self.position += (self.velocity * dt)

