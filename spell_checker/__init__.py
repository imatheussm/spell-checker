from spell_checker.CharacterTree import *
from spell_checker.RadixTree import *
from string import punctuation
from spell_checker.misc import *
#from random import random

def from_dict(data,type,tree=None,low_memory=True):
	"""Convert files with one word per line into a CharacterTree object.

	Parameters
	----------
	data : str (path)
		The path to a file containing words to be loaded into the CharacterTree or RadixTree to be returned. There must be a word per line.
	tree : bool (default = None)
		The CharacterTree or RadixTree object in which the words are meant to be loaded. If not provided, will create a new CharacterTree object.
	low_memory : bool (default = True)
		In hopes of mitigating the load time without multi-threading nor other advanced stuff, this parameter was created. The idea was that if I loaded all words in memory instead of working with them one-at-a-time through the word_generator() generator, the processing time would decrease. In reality, though, after some testing the result was actually the opposite: when low_memory was set to True, the average processing time slightly increased.

	Returns
	-------
	CharacterTree, RadixTree
		A CharacterTree or RadixTree object containing the loaded words provided.
	"""
	try: type = type.lower()
	except: raise TypeError("The type parameter must be a string.")
	if type!="radix" and type!="character": raise ValueError("The available types are 'tree' and 'character'.")
	if tree == None:
		if type=="character": tree = CharacterTree()
		else: tree = RadixTree()
	elif not isinstance(tree,CharacterTree) and not isinstance(tree,RadixTree): raise TypeError("Parameter tree must be a CharacterTree or RadixTree object.")
	with open (data,"r",encoding="utf-8") as file:
		if low_memory == True:
			for word in word_generator(file):
				#if random()<0.1: print(word)
				tree.insert(word)
		else:
			for word in [word.strip("\n") for word in file.readlines()]: tree.insert(word)
	return tree

def from_txt(data,type,tree=None):
	"""Loads words into a CharacterTree from the text file provided.

	Parameters
	----------
	data : str (path)
		The path to a text file containing words to be loaded into the CharacterTree to be returned.
	character_tree : bool (default = None)
		The CharacterTree object in which the words are meant to be loaded. If not provided, will create a new CharacterTree object.

	Returns
	-------
	CharacterTree
		A CharacterTree object containing the loaded words.
	"""
	try: type = type.lower()
	except: raise TypeError("The type parameter must be a string.")
	if type!="radix" and type!="character": raise ValueError("The available types are 'tree' and 'character'.")
	if tree == None:
		if type=="character": tree = CharacterTree()
		else: tree = RadixTree()
	elif not isinstance(tree,CharacterTree) and not isinstance(tree,RadixTree): raise TypeError("Parameter character_tree must be a CharacterTree object.")
	with open (data,"r",encoding="utf-8") as file:
		lines, words = [word.strip("\n") for word in file.readlines()], []
		for line in lines:
			for word in line.split(" "):
				word = ''.join(character for character in word if character not in punctuation)
				#print(word)
				if word.isalpha():
					try: tree.insert(word)
					except: pass
	return tree

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