import asyncio
import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from constants import PLAYER_TURN_SPEED
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

async def play(screen, clock):
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
                return "quit"
        screen.fill("black")
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            result = obj.collides_with(player)
            if result:
                log_event("player_hit")
                print("Game Over!")
                return "dead"
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
        await asyncio.sleep(0)  # yield to browser event loop (pygbag); no-op pause on desktop


async def game_over(screen):
    font = pygame.font.Font(None, 64)
    small = pygame.font.Font(None, 32)
    title = font.render("Game Over", True, "white")
    hint = small.render("Press R to restart", True, "white")
    screen.blit(title, title.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30)))
    screen.blit(hint, hint.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30)))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return "restart"
        await asyncio.sleep(0)


async def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    while True:
        if await play(screen, clock) == "quit":
            return
        if await game_over(screen) == "quit":
            return

    
         
        
























if __name__ == "__main__":
    asyncio.run(main())
