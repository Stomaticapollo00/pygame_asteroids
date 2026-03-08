# Global Import
import pygame
import random

# Local Imports
from circleshape import CircleShape
from logger import log_event
from constants import *

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

    # splits the asteroid into two new, smaller, faster asteroids
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20, 50)
            rotated_vector_1 = self.velocity.rotate(new_angle)
            rotated_vector_2 = self.velocity.rotate(-new_angle)
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_1.velocity = rotated_vector_1 * 1.2
            new_asteroid_2.velocity = rotated_vector_2 * 1.2

