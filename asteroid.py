from circleshape import CircleShape
import pygame
import random
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
            
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_vec1 = self.velocity.rotate(angle)
        new_vec2 = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x,self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x,self.position.y, new_radius)
        new_asteroid1.velocity = new_vec1 * 1.2
        new_asteroid2.velocity = new_vec2 * 1.2

            
            
            
            
        
