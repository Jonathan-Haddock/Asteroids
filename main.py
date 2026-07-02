import pygame
import sys
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import PLAYER_TURN_SPEED
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            result = obj.collides_with(player)
            if result:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for obj in asteroids:
            for shot in shots:
                if  obj.collides_with(shot):
                    obj.split()
                    log_event("asteroid_shot")
                    shot.kill()
                    break
                
            
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        log_state()

    
         
        
























if __name__ == "__main__":
    main()
