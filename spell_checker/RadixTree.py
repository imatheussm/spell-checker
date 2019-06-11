from spell_checker.Radix import *
from spell_checker.misc import get_radices

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

	def find_radix(self,radix,tree):
		"""Finds a radix and returns its index.

		Parameters
		----------
		self : RadixTree
			A RadixTree object.
		radix : str
			The radix to be found
		tree : RadixTree
			The RadixTree object where the search will take place.

		Returns
		-------
		int
			The index of the radix in the tree.next_radices array. Returns -1 if not found.
		"""
		if not isinstance(tree,RadixTree): raise TypeError("The tree parameter must be of type RadixTree.")
		for i in range(len(tree.next_characters)):
			if radix in tree.next_characters[i]: return i
		return -1

	def insert(self,word,tree):
		"""Inserts a word in the CharacterTree.

		It will travel through the existing Character objects, appending new ones to the previous ones if needed, and will mark the last character of the word as final. In other words, for this final character, the is_final attribute will be set to true.

		Parameters
		----------
		self : CharacterTree
			A CharacterTree object.
		word : str
			The word string to be added. A ValueError will be raised if other object type is provided.

		To-do
		-----
		Find the radix in the tree:
			If found, will call recursively the method, with the remaining suffix.
			If not, will check the length of the remaining word:
				If len(word)>0, will add the remaining word under a Character object.
				Else, will verify if the word is final:
					If it is, do nothing.
					Else, set is_final to True.

		"""
		if not isinstance(word,str): raise TypeError("Only strings can be added to CharacterTree objects.")
		for i in list(range(10)) + ["*"]:
			if str(i) in word: raise ValueError("Non-allowed characters were found in the word. Did your word contain any number or \"*\" as a character?")
		#Finding the radix in the Tree among all the possibilities
		pointer, next_radices, radices, result = self, [radix.radix for radix in self.next_radices], get_radices(word)[::-1], False
		for radix in radices:
			for i in range(next_radices):
				pass
		if result: self.find_radix(radix,pointer)
