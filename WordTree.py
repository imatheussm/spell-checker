from os import getcwd
from sys import path as sys_path
sys_path.append(getcwd())
from Character import *

class LetterTree:
	"""Tree of letters, where each path, if final, represents a word.

	Originally named WordTree, its name was changed because, in spite of representing words (or their non-existence), at the end of the day it comes down to a mere hierarchy of letters.
	"""
	def __init__(self,):
		"""
		"""
		pass