# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog plug-in
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class KeepOuterShapes(FilterWithoutDialog):
	
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Keep Outer Shapes',
			'de': 'Umrisse behalten',
			})

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		layer.removeOverlap()
		layer.correctPathDirection()
		for i in range(len(layer.shapes))[::-1]:
			shape = layer.shapes[i]
			if type(shape) == GSPath and shape.direction == 1:
				del(layer.shapes[i])
		layer.correctPathDirection()

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
