# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
   
    # Create Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids  = pygame.sprite.Group()
    
    #Set containers for all classes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #create player and asteroid field instances
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Update all updatable objects   
        updatable.update(dt)
        
        #Set game backgrould
        screen.fill("black")

        #Draw all drawable objects
        for draw in drawable:
            draw.draw(screen)
        
        #Refresh the display
        pygame.display.flip()

        #Limit to 60 FPS and get delta time
        dt = clock.tick(60) / 1000

	

if __name__ == "__main__":
    main()
