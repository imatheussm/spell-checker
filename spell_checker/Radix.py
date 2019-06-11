from spell_checker.Character import *

class Radix:
	""""""
	def __contains__(self,other):
		"""Checks if the radix held by the Radix object is equal to the string provided.

		Parameters
		----------
		self : Radix
			A Radix object.
		other : str
			Although anything can be tested here, since only strings are radices, only strings are meant to be inserted here.

		Returns
		-------
		bool
			The result of the comparison.
		"""
		try: return other in self.radix
		except: return False

	def __eq__(self,other):
		"""Checks if two Radix objects contain the same radices (and previous and next as well).

		In other words: checks if the three attributes (radix, previous_radix and next_radices) are the same.

		Parameters
		----------
		self : Radix
			A Radix object, which will be the reference of the comparison.
		other : Radix
			Another Radix object against which the comparison will be made.

		Returns
		-------
		bool
			The result of the comparison.
		"""
		if isinstance(other,Radix): return self.radix == other.radix and self.previous_radix == other.previous_radix and self.next_radices == other.next_radices
		elif isinstance(other,str): return self.radix == other
		else: return False

	def __gt__(self,other):
		"""Compares the radices incapsulated in the Radix classes, disregarding the previous and next ones.

		Parameters
		----------
		self : Radix
			A Radix object, which will be the reference of the comparison.
		other : Radix
			Another Radix object against which the comparison will be made.

		Returns
		-------
		bool
			The result of the comparison.

		Examples
		--------
		This example takes advantage of this (__gt__()) method.
		>>> "aeho" > "aehu"
		False
		>>> Radix("aeho") > Radix("aehu")
		False

		This one takes advantage of the __lt__() method.
		>>> "aeho" < "aehu"
		True
		>>> Radix("aeho") < Radix("aehu")
		True
		"""
		try: return self.radix > other.radix
		except: return False

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
		self.is_final = True

	def __lt__(self,other):
		"""Compares the characters incapsulated in the Radix classes, disregarding the previous and next ones.

		Parameters
		----------
		self : Radix
			A Radix object, which will be the reference of the comparison.
		other : Radix
			Another Radix object against which the comparison will be made.

		Returns
		-------
		bool
			The result of the comparison.

		Examples
		--------
		This example takes advantage of this (__gt__()) method.
		>>> "aeho" > "aehu"
		False
		>>> Radix("aeho") > Radix("aehu")
		False

		This one takes advantage of the __lt__() method.
		>>> "aeho" < "aehu"
		True
		>>> Radix("aeho") < Radix("aehu")
		True
		"""
		try: return self.radix < other.radix
		except: return False

	def __repr__(self):
		"""Radix representation.

		Shows the character held by the Radix class, as well as the previous one (parent) and next ones (children).

		Parameters
		----------
		self : Radix
			A Radix object.

		Returns
		-------
		str
			The representation of the Character object, containing the aforementioned characteristics.
		"""
		return "<Radix object>\n         Radix: {}\nPrevious Radix: {}\n  Next Radices: {}".format(self.radix,
																												   self.previous_radix,
																												   ", ".join([radix.radix for radix in self.next_radices]))


	def __str__(self):
		"""Converts the radix into a string, omitting previous and next ones.

		Parameters
		----------
		self : Radix
			A Radix object.

		Returns
		-------
		str
			The string representation of the Radix object, which simply is the self.radix attribute.
		"""
		return self.radix