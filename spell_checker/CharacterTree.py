from os import getcwd
from sys import path as sys_path
sys_path.append(getcwd())
from spell_checker.Character import *
from time import sleep

class CharacterTree(Character):
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
			pointer = self
			for letter in other:
				if letter in pointer.next_characters: pointer = pointer.next_characters[pointer.next_characters.index(letter)]
				else: return False
			return pointer.is_final
		else:
			return False

	def __init__(self,*args):
		"""Constructor of the CharacterTree class.

		Parameters
		----------
		self : CharacterTree
			A CharacterTree object.
		*args : list, str, tuple
			All the remaining parameters shall be added as words of this CharacterTree. If an argument is of type list or tuple, each of its elements will be added individually as well. If a string is provided as an argument, it will be normally added. Otherwise, an Exception will be raised during addition.

		Returns
		-------
		CharacterTree
			A CharacterTree object, containing the elements provided in *args as possible words (if any).
		"""
		super().__init__('*')
		self.is_final = True
		self.loaded_words = 0
		for arg in args:
			if isinstance(arg,list) or isinstance(arg,tuple):
				for item in arg: self.insert(item)
			else: self.insert(arg)

	def __iter__(self,current_word=[],next_characters=None):
		"""Iterator capability of CharacterTree.

		Serves to deliver all the words in the CharacterTree.
		"""
		if next_characters == None: next_characters = self.next_characters
		raise NotImplementedError("I have been facing some difficulties with this. I'll leave this to tomorrow.")

	def __repr__(self):
		"""Representation of the CharacterTree object.

		Parameters
		----------
		self : CharacterTree
			A CharacterTree object.

		Returns
		-------
		str
			The string representation of the object.
		"""
		return "<CharacterTree object>\n{} words loaded.\nAvailable Initial Characters: {}".format(self.loaded_words,
																								   ", ".join([character.character for character in self.next_characters]))

	def check(self,path):
		"""Checks a text for mis-spellings.

		Parameters
		----------
		self : CharacterTree
			A CharacterTree object.
		path : str (path)
			The path to the file to be spell-checked.

		Returns
		-------
		tuple
			A tuple containing all the unknown words.
		"""
		with open(path, "r", encoding="utf-8") as file:
			misspellings = []
			for word in [line.strip("\n").split(" ") for line in file.readlines()]:
				if word[0] not in self: misspellings.append(word)
		return misspellings


	def insert(self,word):
		"""Inserts a word in the CharacterTree.

		It will travel through the existing Character objects, appending new ones to the previous ones if needed, and will mark the last character of the word as final. In other words, for this final character, the is_final attribute will be set to true.

		Parameters
		----------
		self : CharacterTree
			A CharacterTree object.
		word : str
			The word string to be added. A ValueError will be raised if other object type is provided.
		"""
		if not isinstance(word,str): raise TypeError("Only strings can be added to CharacterTree objects.")
		for i in list(range(10)) + ["*"]:
			if str(i) in word: raise ValueError("Non-allowed characters were found in the word. Did your word contain any number or \"*\" as a character?")
		pointer = self
		for letter in word:
			if letter in pointer.next_characters: pointer = pointer.next_characters[pointer.next_characters.index(letter)]
			else:
				pointer.next_characters.append(Character(letter,pointer))
				for index in range(len(pointer.next_characters)):
					if pointer.next_characters[index].character==letter:
						pointer = pointer.next_characters[index]
						break
		if pointer.is_final == False:
			pointer.is_final = True
			self.loaded_words += 1
		else: raise ValueError("Provided word ({}) already exists in this CharacterTree object.".format(word))

	def remove(self,word):
		"""Removes a word from the CharacterTree.

		It will travel through the Characters, raising a ValueError if a character of the word is not found (because it doesn't exist in the tree to be removed in the first place). If the word is found, the is_final attribute will be checked: if True, it will be set to False. If it is False in the first place, a ValueError will be raised (the word, again, was not found). Then, if there are no "children" of this "node" object (if the next_characters list contained in the Character object is empty), then the algorithm will delete the non-final characters until it gets to a final one, where it will stop, assuring that all the peripheral Character objects are always final.

		Parameters
		----------
		self : CharacterTree
			A CharacterTree object.
		word : str
			A word string to be removed from the CharacterTree object.
		"""
		if not isinstance(word,str): raise TypeError("The word parameter type must be str.")
		pointer = self
		for letter in word:
			if letter in pointer.next_characters: pointer = pointer.next_characters[pointer.next_characters.index(letter)]
			else: raise ValueError("This word is not contained in this CharacterTree.")
		if pointer.is_final==True: pointer.is_final = False
		else: raise ValueError("This word is not contained in this CharacterTree.")
		if len(pointer.next_characters) == 0:
			while not pointer.is_final:
				previous_pointer = pointer.previous_character
				previous_character.next_characters.remove(pointer)
				pointer = previous_pointer
		self.loaded_words-=1