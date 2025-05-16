import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS, PLAYER_SHOOT_SPEED # import constants
from circleshape import CircleShape  # import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        # Check if the shot is out of bounds
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
            self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()