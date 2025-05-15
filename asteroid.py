import pygame
import random
import math
from constants import * # import constants
from circleshape import CircleShape  # import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

            # Generate polygon points once during creation
        num_points = random.randint(6, 10)
        self.points_offsets = []
    
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            # Vary the radius a bit for each point
            point_radius = radius * random.uniform(0.8, 1.2)
            offset_x = math.cos(angle) * point_radius
            offset_y = math.sin(angle) * point_radius
            self.points_offsets.append((offset_x, offset_y))
        
    def draw(self, screen):
        points = []
        for offset_x, offset_y in self.points_offsets:
            point_x = self.position.x + offset_x
            point_y = self.position.y + offset_y
            points.append((point_x, point_y))
    
    # Draw the polygon
        pygame.draw.polygon(screen, "white", points, 2)  # 2 is the line width
        #pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt