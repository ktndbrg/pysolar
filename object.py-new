import math
import pygame

"""
	Generic object class
"""
class Object ():
	"""
		Initialize the Object
		image = "planet.png"	# filename of the sprite to use
		position = None,		# (300, 300), position of start
		scale = None,			# scaling the sprite
	"""
	def __init__ (self, posisjon = None, bilde = "planet.png", skalering = None):
		# Image to be used as a planet
		self.sprite = pygame.image.load(bilde).convert_alpha()

		# Did the image need to be scaled?
		if skalering is not None:
			self.sprite = pygame.transform.scale (self.sprite, skalering)

		# Set the position
		self.posisjon = posisjon

	"""
		This method is called every frame.
		Update the game-physics (game logic) on the planet
		clock: pygame clock object. This has the delta_time
	"""
	def update (self, clock):
		pass

	"""
		This method will render the object onto the screen
	"""
	def render (self, screen):
		screen.blit (self.sprite,
					(self.posisjon[0] - (self.sprite.get_width () / 2.0), self.posisjon[1] - (self.sprite.get_height () / 2.0)))

