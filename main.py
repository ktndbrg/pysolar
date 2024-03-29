import math
import random
import pygame

from star import Star
from planet import Planet

"""
    Game Class
"""
class Game ():

    """
        Initialize all the subsystems for the game engine.
    """
    def __init__ (self):
        # Start up pygame
        pygame.init ()
        
        # Create the application window
        self.screen = pygame.display.set_mode ((800, 800), flags = pygame.SCALED)
        # Set the Title of the window
        pygame.display.set_caption ("NordNorsk Vitensenter - Kodeklubb")
        
        # Create a Star object
        self.star = Star (position = [x * 0.5 for x in self.screen.get_size ()],
                        scale = [x * 0.15 for x in self.screen.get_size ()])

        # Create a Planet object
        self.planets = [Planet (image = "planet.png",
                                angle = random.random() * 2.0 * math.pi,
                                radius = 250,
                                speed = random.random(),
                                scale = (64, 64)) for _ in range (0, 5)]
        
        # Create moons
        self.moons = [Planet (image = "planet2.png",
                                angle = random.random() * 2.0 * math.pi,
                                radius = 100,
                                speed = 10 * random.random(),
                                scale = (16, 16)) for _ in range (0, 5)]

        # We need to track time, with a clock
        self.clock = pygame.time.Clock ()
        # Set the framerate (FPS) to 60 fps
        self.clock.tick (60)

    """
        This method (function) starts the game loop
    """
    def run (self):
        # The game will run if run_flag == True
        self.run_flag = True

        # This is the game loop
        while self.run_flag == True:
            # This checks keyboard inputs
            self.events ()

            # Update the game logic and physics
            self.update ()

            # Render all the visuals
            self.render ()

            # A frame has passed, tick the clock
            self.clock.tick (60)

        # Cleanup afterwards
        pygame.quit ()
        quit ()

    """
        Check for game inputs/events
    """
    def events (self):
        """
            You can find all the keycode from this website:
            https://www.pygame.org/docs/ref/key.html
        """
        # Loop through every event that has happened
        for event in pygame.event.get ():
            # Did we click EXIT?
            if event.type == pygame.QUIT:
                self.run_flag = False
            
            # A Key was pressed
            elif event.type == pygame.KEYDOWN:

                # Quit the game if button 'q' is pressed
                if event.key == pygame.K_q:
                    self.run_flag = False

                # Speedup
                elif event.key == pygame.K_LEFT:
                    for planet in self.planets:
                        planet.speed *= 1.5
                elif event.key == pygame.K_RIGHT:
                    for planet in self.planets:
                        planet.speed *= 0.75

                # Increase radius
                elif event.key == pygame.K_UP:
                    for planet in self.planets:
                        planet.radius *= 1.2
                elif event.key == pygame.K_DOWN:
                    for planet in self.planets:
                        planet.radius *= 0.8

    """
        Update the game logic
    """
    def update (self):
        # Update the planets
        #for planet in self.planets:
        #    planet.update (self.clock, self.star.position)

        for planet, moon in zip(self.planets, self.moons):
            planet.update (self.clock, self.star.position)
            moon.update (self.clock, planet.position)

    """
        Render the graphics
    """
    def render (self):
        # Fill the screen with colour DARK_GREY
        DARK_GREY = (25, 25, 25)
        self.screen.fill (DARK_GREY)

        # Render the star
        self.star.render (self.screen)

        # Render the planets
        for planet in self.planets:
            planet.render (self.screen)

        for moon in self.moons:
            moon.render (self.screen)

        # Flip the table
        pygame.display.flip ()

"""
    This will run when you execute the program (.exe file)
"""
if __name__ == "__main__":
    # Create a new Game object
    game = Game ()

    # Let's start the game
    game.run ()

