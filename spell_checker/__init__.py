from spell_checker.CharacterTree import *
#from random import random

def from_csv(data,low_memory=True):
	"""Convert a CSV file into a CharacterTree object.

	Parameters
	----------
	data : str
		The path to a .csv file containing words to be loaded into the CharacterTree to be returned.
	low_memory : bool (default = True)
		In hopes of mitigating the load time without multi-threading nor other advanced stuff, this parameter was created. The idea was that if I loaded all words in memory instead of working with them one-at-a-time through the word_generator() generator, the processing time would decrease. In reality, though, after some testing the result was actually the opposite: when low_memory was set to True, the average processing time slightly increased.

	Returns
	-------
	CharacterTree
		A CharacterTree object containing the loaded words.
	"""
	character_tree = CharacterTree()
	with open (data,"r",encoding="utf-8") as file:
		if low_memory == True:
			for word in word_generator(file):
				#if random()<0.1: print(word)
				character_tree.insert(word)
		else:
			words = file.readlines()
			words = [word.strip("\n") for word in words]
			for word in words:
				character_tree.insert(word)
	return character_tree

def word_generator(data,case_sensitive=True):
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
	words = iter(data)
	if case_sensitive==True:
		for word in words:
			yield word.strip("\n")
	else:
		for word in words:
			yield word.lower().strip("\n")