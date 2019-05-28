from spell_checker.CharacterTree import *
from random import random

def from_csv(data):
	"""Convert a CSV file into a CharacterTree object.

	Parameters
	----------
	data : str
		The path to a .csv file containing words to be loaded into the CharacterTree to be returned.

	Returns
	-------
	CharacterTree
		A CharacterTree object containing the loaded words.
	"""
	character_tree = CharacterTree()
	with open (data,"r",encoding="utf-8") as file:
		for word in words(file):
			if random()<0.1: print(word)
			character_tree.insert(word)
	return character_tree

def words(data,case_sensitive=True):
	"""Word generator.

	Parameters
	----------
	data : str
		The data to be turned into words of the CharacterTree object.
	case_sensitive : bool
		Tells if the words are meant to be case-sensitive. If not, everything is set to lowercase.

	Returns
	-------
	CharacterTree
		A CharacterTree object with the words of the file loaded.
	"""
	lines = iter(data)
	if case_sensitive==True:
		for line in lines:
			for word in line.split():
				if word.isalpha(): yield word
	else:
		for line in lines:
			for word in line.lower().split():
				if word.isalpha(): yield word