from spell_checker.Radix import *


class RadixTree(Radix):
	"""Tree of letters, where each path, if final, represents a word.

	Originally named WordTree (and then LetterTree), its name was changed because, in spite of representing words (or their non-existence), at the end of the day it comes down to a mere hierarchy of characters.
	"""
	def __contains__(self,other):
		"""Checks if a word is contained in the CharacterTree.

		In other words, checks if all characters are present in the object and if the last one is considered final.

		Parameters
		----------
		self : CharacterTree
			A CharacterTree object.
		other : str
			A string (word) whose existance in the CharacterTree is to be checked.

		Returns
		-------
		bool
			The result of the verification.
		"""
		if isinstance(other,str):
			raise NotImplementedError("To be implemented.")
		else:
			return False

	def __init__(self,*args):
		"""Constructor of the RadixTree class.

		Parameters
		----------
		self : RadixTree
			A RadixTree object.
		*args : list, str, tuple
			All the remaining parameters shall be added as words of this RadixTree. If an argument is of type list or tuple, each of its elements will be added individually as well. If a string is provided as an argument, it will be normally added. Otherwise, an Exception will be raised during addition.

		Returns
		-------
		RadixTree
			A RadixTree object, containing the elements provided in *args as possible words (if any).
		"""
		super().__init__('*')
		self.is_final = True
		self.loaded_words = 1
		for arg in args:
			if isinstance(arg,list) or isinstance(arg,tuple):
				for item in arg: self.insert(item)
			else: self.insert(arg)