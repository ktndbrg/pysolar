import math
import pygame

from object import Object

"""
	Star class
"""
class Star (Object):
	"""
		Initialize the Star
	"""
	def __init__ (self, position, scale = None):
		# This calls the Object constructor
		super().__init__ (position = position, image = "star.png", scale = scale)

