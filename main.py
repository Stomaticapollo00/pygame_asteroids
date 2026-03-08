# Global Import
import pygame
import sys

# Local Imports
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    # Initialize Game and Setup Screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Set Sprite Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set Player Sprite
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Set Asteroid Sprite
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set Shot Sprite
    Shot.containers = (shots, updatable, drawable)

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
        dt = clock.tick(60) / 1000                  # FPS/clockspeed
        screen.fill("black")                        # set background color
        updatable.update(dt)                        # update updatable sprites
        for asteroid in asteroids:                  # loop asteroid checker for collisions
            if asteroid.collides_with(player):      # if player hit log the event and end game
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:                  # loop asteroid checker for collisions
            for shot in shots:                      # loop shot checker for collisions
                if shot.collides_with(asteroid):    # if asteroid hit by shot log the event and kill sprites
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()
        for sprite in drawable:                     # loop for drawble sprites
            sprite.draw(screen)                     # draw new sprite position
        pygame.display.flip()                       # output to display

    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
