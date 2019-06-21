from spell_checker.Radix import *

class RadixTree(Radix):
	"""Tree of letters, where each path, if final, represents a word.

	Originally named WordTree (and then LetterTree), its name was changed because, in spite of representing words (or their non-existence), at the end of the day it comes down to a mere hierarchy of characters.
	"""
	def __contains__(self,other,tree=None):
		"""Checks if a word is contained in the CharacterTree.

		In other words, checks if all characters are present in the object and if the last one is considered final.

		Parameters
		----------
		self : CharacterTree
			A CharacterTree object.
		other : str
			A string (word) whose existance in the CharacterTree is to be checked.
		tree : Radix, NoneType (default = None)
			Due to the recursive nature of this method, this keyworded attribute is employed in the recursive call. If left with the default value, the object itself will be set as tree.

		Returns
		-------
		bool
			The result of the verification.
		"""
		if isinstance(other,str):
			#Finding the radix in the Tree among all the possibilities
			if tree == None:
				#print("No tree was defined.  Defining tree to be self...")
				tree = self
			#else: print("tree = {} | word: {}".format(tree.radix,other))
			if other == "": return True
			if len(other) > 0:
				if len(tree.next_radices) > 0:
					#print("There are children!  Analyzing one-by-one...")
					for next_radix in tree.next_radices:
						#print("Current radix: {}".format(next_radix.radix))
						try:
							for i in range(len(next_radix.radix)):
								if next_radix.radix[i] != other[i]:
									break
								else:
									if i == len(next_radix.radix) - 1: return self.__contains__(other[i + 1:],next_radix)
						except IndexError:
							continue
					#print("None of the words are related!  Returning False.")
					return False
				else:
					#print("There are no children!  Returning False.")
					return False
			else:
				#print("Word processed!  Returning .is_final.")
				return tree.is_final
		else:
			#print("The other parameter is not a string object!  Returning False.")
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
			A RadixTree object containing the elements provided in *args as possible words (if any).
		"""
		super().__init__('*')
		self.is_final = True
		self.loaded_words = 1
		for arg in args:
			if isinstance(arg,list) or isinstance(arg,tuple):
				for item in arg: self.insert(item)
			else: self.insert(arg)

	def __repr__(self):
		"""Representation of the RadixTree object.

		Parameters
		----------
		self : RadixTree
			A CharacterTree object.

		Returns
		-------
		str
			The string representation of the object.
		"""
		self.next_radices.sort()
		return "<RadixTree object>\n{} words loaded.\nAvailable Initial Radices: {}".format(self.loaded_words,
																								   ", ".join([radix.radix for radix in self.next_radices]))

	def check(self,path):
		"""Checks a text for mis-spellings.

		Parameters
		----------
		self : RadixTree
			A RadixTree object.
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

	def insert(self,word,tree=None):
		"""Inserts a word in the CharacterTree.

		It will travel through the existing Character objects, appending new ones to the previous ones if needed, and will mark the last character of the word as final. In other words, for this final character, the is_final attribute will be set to true.

		Parameters
		----------
		self : CharacterTree
			A CharacterTree object.
		word : str
			The word string to be added. A ValueError will be raised if other object type is provided.
		tree : Radix, NoneType (default = None)
			Due to the recursive nature of this method, this keyworded attribute is employed in the recursive call. If left with the default value, the object itself will be set as tree.

		"""
		if not isinstance(word,str): raise TypeError("Only strings can be added to CharacterTree objects.")
		for i in list(range(10)) + ["*"]:
			if str(i) in word: raise ValueError("Non-allowed characters were found in the word. Did your word contain any number or \"*\" as a character?")
		#Finding the radix in the Tree among all the possibilities
		if tree == None:
			#print("No tree was defined.  Defining tree to be self...")
			tree = self
		#else: print("tree = {} | word: {}".format(tree.radix,word))
		if len(word) > 0:
			if len(tree.next_radices) > 0:
				#print("There are children!  Analyzing one-by-one...")
				for next_radix in tree.next_radices:
					#print("Current radix: {}".format(next_radix.radix))
					try:
						for i in range(len(next_radix.radix)):
							if next_radix.radix[i] != word[i]:
								#print("{} is not equal to {}!".format(next_radix.radix[i],word[i]))
								if i == 0: break
								else:
									if len(word[i:]) > 0:
										#print("There's a relation, but there's a suffix!  Calling
										#.insert()...\n")
										new_next_radices = next_radix.next_radices
										#print("new_next_radices: {}".format(new_next_radices))
										#print("new Radix
										#object:\n{}".format(Radix(next_radix.radix[i:],next_radix,new_next_radices).__repr__()))
										next_radix.next_radices = [Radix(next_radix.radix[i:],next_radix,new_next_radices)]
										next_radix.radix = word[:i]
										next_radix.is_final = False
										for radix in new_next_radices: radix.previous_radix = next_radix.next_radices[0]
										del(new_next_radices)
										return self.insert(word[i:],next_radix)
									else:
										if next_radix.is_final == True: raise ValueError("The word {} has already been inserted!".format(word[:i]))
										else:
											next_radix.is_final = True
											self.loaded_words += 1
							else:
								if i == len(next_radix.radix) - 1: return self.insert(word[i + 1:],next_radix)
					except IndexError:
						#print("The word {} is contained in {}!  Making proper adjustments...\n".format(word,next_radix.radix))
						new_next_radices = next_radix.next_radices
						#print("new_next_radices: {}".format(new_next_radices))
						#print("new Radix
						#object:\n{}".format(Radix(next_radix.radix[i:],next_radix,new_next_radices).__repr__()))
						next_radix.next_radices = [Radix(next_radix.radix[i:],next_radix,new_next_radices)]
						next_radix.radix = word
						for radix in new_next_radices: radix.previous_radix = next_radix.next_radices[0]
						del(new_next_radices)
						self.loaded_words += 1
						return
						#if tree.is_final == False:
						#	tree.is_final = True
						#	self.loaded_words += 1
				#print("None of the words are related!  Appending...")
				tree.next_radices.append(Radix(word,tree))
				self.loaded_words += 1
			else:
				#print("There are no children!  Appending...")
				tree.next_radices.append(Radix(word,tree))
				self.loaded_words += 1
		else:
			#print("Word processed!")
			if tree.is_final == False:
				tree.is_final = True
				self.loaded_words += 1

	def remove(self,word,tree=None):
		"""

		Parameters
		----------
		self : RadixTree
			A RadixTree object.
		word : str
			A string (word) whose existance in the RadixTree is to be checked.
		tree : Radix (default = None)
			Due to the recursive nature of this method, this keyworded attribute is employed in the recursive call. If left with the default value, the object itself will be set as tree.
		"""
		if isinstance(word,str):
			#Finding the radix in the Tree among all the possibilities
			if tree == None:
				#print("No tree was defined.  Defining tree to be self...")
				tree = self
			#else: print("tree = {} | word: {}".format(tree.radix,word))
			if len(word) > 0:
				if len(tree.next_radices) > 0:
					#print("There are children!  Analyzing one-by-one...")
					for next_radix in tree.next_radices:
						#print("Current radix: {}".format(next_radix.radix))
						try:
							for i in range(len(next_radix.radix)):
								if next_radix.radix[i] != word[i]: break
								elif i == len(next_radix.radix) - 1: return self.remove(word[i + 1:],next_radix)
						except IndexError: continue
					raise ValueError("The word {} is not contained in this RadixTree.".format(word))
				else: raise ValueError("The word {} is not contained in this RadixTree.".format(word))
			else:
				if tree.is_final == True:
					#print("{} is in the RadixTree! Removing...".format(word))
					previous_radix, tree.is_final = tree.previous_radix, False
					self.loaded_words -= 1
					while tree.is_final == False and tree.radix != "*":
						#print("Attempting to optimize RadixTree...")
						if len(tree.next_radices) == 0:
							#print("len(tree.next_radices)==0. Removing {}...".format(tree.radix))
							previous_radix.next_radices.remove(tree)
						elif len(tree.next_radices) == 1:
							#print("len(tree.next_radices)==1. Merging {} with {}...".format(tree.radix,tree.next_radices[0].radix))
							tree.radix += tree.next_radices[0].radix
							tree.next_radices += tree.next_radices[0].next_radices
							tree.is_final, tree.next_radices = True, tree.next_radices[1:]
							for radix in tree.next_radices:
								radix.previous_radix = tree
						else: break
						tree, previous_radix = previous_radix, tree.previous_radix

		else: raise TypeError("The other parameter is not a string object.")