from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity, spawner):
        super().__init__(x, y, radius)
        self.spawner = spawner
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        pygame.sprite.Sprite.kill(self)

        if (self.radius <= ASTEROID_MIN_RADIUS):
            return

        random_angle = random.uniform(20, 50)
        first_asteroid_velocity = self.velocity.rotate(random_angle)
        second_asteroid_velocity = self.velocity.rotate(random_angle * -1)

        split_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        self.spawner.spawn(split_asteroid_radius, self.position.x, self.position.y, first_asteroid_velocity)
        self.spawner.spawn(split_asteroid_radius, self.position.x, self.position.y, second_asteroid_velocity)