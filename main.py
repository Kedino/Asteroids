import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT  #import constants
from circleshape import CircleShape # import CircleShape
from player import Player   # import Player
from asteroidfield import AsteroidField # import AsteroidField
from asteroid import Asteroid # import Asteroid
from shot import Shot # import Shot

#import os

#print(f"Current working directory: {os.getcwd()}")
#print(f"Files in directory: {os.listdir('.')}")

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                return

        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        #player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
