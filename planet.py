import math
import pygame

from object import Object

"""
	Planet class
"""
class Planet (Object):
	"""
		Initialize the Planet
		bilde = "planet.png"	# filename of the sprite to use
		vinkel = 0.0,			# starting position
		radius = 50.0,			# distance from the star
		hastighet = 1.5,		# speed of rotation
		skalering = None		# scaling the image
	"""
	def __init__ (self, bilde = "planet.png", vinkel = math.pi, radius = 50.0, hastighet = 1.5, skalering = None):
		# Initialize the Object
		super().__init__ (bilde = bilde, skalering = skalering)

		# Radius of the orbit
		self.radius = 250

		# The starting angle
		self.vinkel = math.pi/4

		# Speed of the planet
		self.hastighet = 0.25

	"""
		This method is called every frame.
		Update the game-physics (game logic) on the planet
		clock: pygame clock object. This has the delta_time
		star: object to orbit
	"""
	def update (self, clock, orbit):
		# Update the angle of the planet
		self.vinkel += self.hastighet * (clock.get_time () / 1000.0)
		
		# We can reset the rotation because "mathematics". Angle = Angle +- 2*n*pi (n is a whole number)
		if self.vinkel > 2*math.pi:
			self.vinkel -= 2*math.pi
		elif self.vinkel < 0.0:
			self.vinkel += 2*math.pi

		# Update the position based on the angle.
		# This is Trigonometry (Mathematics)
		# x**2 + y**2 = r**2, where r is the radius of the circle.
		self.posisjon = [orbit[0] + self.radius * math.cos (self.vinkel), orbit[1] - self.radius * math.sin (self.vinkel)]

	"""
		This method will render the planet onto the game-screen
	"""
	def render (self, screen):
		# Create a temporary sprite, we rotate this temp, and display it.
		# This makes it easier to rotate on the next frame.
		temp = self.sprite
		self.sprite = pygame.transform.rotate (self.sprite, (self.vinkel - (math.pi / 2.0)) * 180 / math.pi)
		# Use the Object method for rendering
		super().render(screen)
		self.sprite = temp

