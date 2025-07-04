import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT  #import constants
from circleshape import CircleShape # import CircleShape
from player import Player   # import Player
from asteroidfield import AsteroidField # import AsteroidField
from asteroid import Asteroid # import Asteroid
from shot import Shot # import Shot
from score import ScoreManager # import ScoreManager
from clock import GameClockManager # import GameClockManager
from controls import KEYSET_WASD, KEYSET_ARROWS  # import control keysets

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player_mode = "single"  # single player by default. multiplayer functionality is not yet implemented
    paused = False  # for future pause implementation
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    ScoreManager.containers = (drawable)
    GameClockManager.containers = (drawable, updatable)

    clock = pygame.time.Clock()
    dt = 0
    score_manager = ScoreManager()
    game_clock = GameClockManager(score_manager)


    asteroid_field = AsteroidField()
    if player_mode == "single": # This is the default mode
        # In single player mode, the player can use both WASD and arrow keys
        player1_controls = [KEYSET_WASD, KEYSET_ARROWS]
        player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, controls = player1_controls)
        players = [player1]
    elif player_mode == "multiplayer":  # This is a placeholder for future multiplayer functionality
        player1_controls = [KEYSET_WASD]
        player2_controls = [KEYSET_ARROWS]
        player1 = Player(SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2, controls=player1_controls)
        player2 = Player(SCREEN_WIDTH / 2 + 50, SCREEN_HEIGHT / 2, controls=player2_controls)
        players = [player1, player2]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids:
            for player in players:
                if asteroid.collide(player):
                    print("Game over!")
                    print(f"Final score: {score_manager.score}")
                    return
            for shot in shots:
                if asteroid.collide(shot):
                    asteroid.split(score_manager)
                    shot.kill()
                    

        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
