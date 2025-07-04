import pygame
from circleshape import CircleShape # import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN # import constants
from shot import Shot # import Shot
from controls import KEYSET_WASD, KEYSET_ARROWS  # import control keysets

class Player(CircleShape):
    def __init__(self, x, y, controls = None):
        super().__init__(x, y, PLAYER_RADIUS)
        self.controls = controls
        self.rotation = 180
        self.shot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        #pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 1)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()
        for control in self.controls:
            if keys[control['left']]:
                self.rotate(-dt)
            if keys[control['right']]:
                self.rotate(dt)
            if keys[control['forward']]:
                self.move(dt)
            if keys[control['backward']]:
                self.move(-dt)
            if keys[control['shoot']]:
                self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_timer > 0:
            return None
        # Create a new shot at the player's position
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot = Shot(self.position.x, self.position.y, self.rotation)
        return shot