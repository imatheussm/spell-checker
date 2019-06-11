from spell_checker.Character import *

class Radix(Character):
	""""""
	def __init__(self,radix,previous_radix = None,*args):
		"""Class builder.

		Parameters
		----------
		self : Radix
			A Radix object.
		radix : str, int
			The radix to be incapsulated into a Radix object. If an integer is provided, it will be automatically converted into a Radix.
		previous_radix : Radix (default = None)
			The parent "Node". A TypeError Exception will be raised if an object of another type is provided.
		*args : str, int
			All remaining parameters eventually provided will be interpreted as next_radices (sons), will be incapsulated into Characters if needed and appended as sons of the current character.
		Returns
		-------
		Radix
			A Radix object.
		"""
		if isinstance(radix,int) or isinstance(radix,Character): radix = str(radix)
		if not isinstance(radix,str): raise TypeError("A Radix object can hold only strings.")
		self.radix = radix#.lower()
		if previous_radix != None and not isinstance(previous_radix,Radix): raise TypeError("The previous radix must be a Radix object as well.")
		else: self.previous_radix = previous_radix
		self.next_radices = sorted([Radix(arg) for arg in args if isinstance(arg,str)])
		self.is_final = False