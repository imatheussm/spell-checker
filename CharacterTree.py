from os import getcwd
from sys import path as sys_path
sys_path.append(getcwd())
from Character import *

class CharacterTree(Character):
	"""Tree of letters, where each path, if final, represents a word.

	Originally named WordTree (and then LetterTree), its name was changed because, in spite of representing words (or their non-existence), at the end of the day it comes down to a mere hierarchy of characters.
	"""
	def __contains__(self,other):
		"""
		"""
		if isinstance(other,int): return False
		if isinstance(other,str):
			pointer = self
			for letter in other:
				if letter in pointer.next_characters: pointer = pointer.next_characters[pointer.next_characters.index(letter)]
				else: return False
			return pointer.is_final

	def __init__(self,*args):
		"""
		"""
		super().__init__('*')
		self.is_final = True
		for arg in args: self.insert(arg)

	def insert(self,word):
		"""
		"""
		if not isinstance(word,str): raise TypeError("Only strings can be added to CharacterTree objects.")
		for i in list(range(10))+["*"]:
			if str(i) in word: raise ValueError("Non-allowed characters were found in the word. Did your word contain any number or \"*\" as a character?")
		pointer = self
		for letter in word:
			if word in pointer.next_characters: pointer = pointer.next_characters[pointer.next_characters.index(letter)]
			else:
				pointer.next_characters.append(Character(letter,pointer))
				pointer = pointer.next_characters[pointer.next_characters.index(letter)]
		pointer.is_final = True

	def remove(self,word):
		"""
		"""
		pointer = self
		for letter in word:
			if letter in pointer.next_characters: pointer = pointer.next_characters[pointer.next_characters.index(letter)]
			else: raise ValueError("This word is not contained in this CharacterTree.")
		pointer.is_final = False
		while not pointer.is_final:
			previous_pointer = pointer.previous_character
			previous_character.next_characters.remove(pointer)
			pointer = previous_pointer