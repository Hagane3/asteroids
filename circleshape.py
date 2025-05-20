import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)

    def update(self, dt):
        pass

    def collision(self, circle):
        distance = pygame.math.Vector2.distance_to(self.position, circle.position)
        sum_radius = self.radius + circle.radius

        if (distance <= sum_radius):
            return True
        
        if (distance > sum_radius):
            return False