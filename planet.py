import math
import pygame

from object import Object

"""
	Planet class
"""
class Planet (Object):
	"""
		Initialize the Planet
		image = "planet.png"	# filename of the sprite to use
		angle = 0.0,			# starting position
		radius = 50.0,			# distance from the star
		speed = 1.5,			# speed of rotation
		scale = None			# scaling the image
	"""
	def __init__ (self, image = "planet.png", angle = math.pi, radius = 50.0, speed = 1.5, scale = None):
		# Initialize the Object
		super().__init__ (image = image, scale = scale)

		# Radius of the orbit
		self.radius = radius

		# The starting angle
		self.angle = angle

		# Speed of the planet
		self.speed = speed

	"""
		This method is called every frame.
		Update the game-physics (game logic) on the planet
		clock: pygame clock object. This has the delta_time
		star: object to orbit
	"""
	def update (self, clock, orbit):
		# Update the angle of the planet
		self.angle += self.speed * (clock.get_time () / 1000.0)
		
		# We can reset the rotation because "mathematics". Angle = Angle +- 2*n*pi (n is a whole number)
		if self.angle > 2*math.pi:
			self.angle -= 2*math.pi
		elif self.angle < 0.0:
			self.angle += 2*math.pi

		# Update the position based on the angle.
		# This is Trigonometry (Mathematics)
		# x**2 + y**2 = r**2, where r is the radius of the circle.
		self.position = [orbit[0] + self.radius * math.cos (self.angle), orbit[1] - self.radius * math.sin (self.angle)]

	"""
		This method will render the planet onto the game-screen
	"""
	def render (self, screen):
		# Create a temporary sprite, we rotate this temp, and display it.
		# This makes it easier to rotate on the next frame.
		temp = self.sprite
		self.sprite = pygame.transform.rotate (self.sprite, (self.angle - (math.pi / 2.0)) * 180 / math.pi)
		# Use the Object method for rendering
		super().render(screen)
		self.sprite = temp

