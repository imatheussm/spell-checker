def get_radices(word,empty_word=False):
	"""Radix generator.

	Parameters
	----------
	word : str
		The word to be sliced into radices.

	Returns
	-------
	list : [str, str, ..., str]
	"""
	if empty_word == True: return [""] + [word[:i] for i in range(1,len(word)+1)]
	return [word[:i] for i in range(1,len(word)+1)]