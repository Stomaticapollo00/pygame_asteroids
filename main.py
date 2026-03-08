# Global Import
import pygame

# Local Imports
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Initialize Game and Setup Screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Set Sprite Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Set Player Sprite
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Set Asteroid Sprite
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set AsteroidField
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    # Set Game Clock
    clock = pygame.time.Clock()
    dt = 0

    # Game Loop
    while True:
        # Close Window Check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Set and Show Display Output
        log_state()
        dt = clock.tick(60) / 1000  # FPS/clockspeed
        screen.fill("black")        # set background color
        updatable.update(dt)        # update updatable sprites
        for sprite in drawable:     # loop for drawble sprites
            sprite.draw(screen)     # draw new sprite position
        pygame.display.flip()       # output to display

    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
