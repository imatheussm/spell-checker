from random import random
from os import getcwd
from sys import path as sys_path
from time import time
sys_path.append(getcwd())
from spell_checker import *

def sample_file(path,new_path,percentage=.20):
	"""Randomly selects lines from files.

	Parameters
	----------
	path : str (path)
		The path of the file to be sampled.
	new_path : str (path)
		The path of the file to be created with the chosen lines.
	percentage : float (default = .20)
		The percentage of lines to be chosen.
	"""
	sample = []
	with open(path,"r",encoding="utf-8") as file:
		line = file.readline()
		while line != "":
			if random() < percentage: sample.append(line)
			line = file.readline()

	with open(new_path,"w",encoding="utf-8") as file:
		for item in sample: file.write(item)

a = CharacterTree("abacate","mamão","maniçoba","queijo")
print("Árvore criada com as palavras \"abacate\", \"mamão\",\"maniçoba\" e \"queijo\" nela.")
print("Há maniçoba nela? Resposta: {}.".format("maniçoba" in a))
print("Há abacate nela?  Resposta: {}.".format("abacate" in a))
print("E aba?            Resposta: {}.".format("aba" in a))
print("Então, adicionemos aba.")
a.insert("aba")
print("A palavra aba adicionada.")
print("Há aba na árvore? Resposta: {}.".format("aba" in a))
print("Perfeito.")

print(", ".join([character.character for character in a.next_characters]))

print("\n\n")

b = RadixTree("abacate","mamão","maniçoba","queijo","menino", "menina")
# b.insert("menino")

#print("Comparing execution times: ",end="")
#start_time = time()
#ct = from_dict("D:\igor\OneDrive\Documentos\GitHub\spell-checker\dictionaries\palavras.txt", "CHARACTER") # 320140 palavras in CharacterTree.
#rt = from_dict("D:\igor\OneDrive\Documentos\GitHub\spell-checker\dictionaries\palavras.txt", "RADIX") # 320140 palavras in CharacterTree.
#elapsed = time() - start_time
#print("{}".format(str(elapsed)))

#start_time = time()
#constituicao = from_txt("D:/igor/OneDrive/Documentos/GitHub/spell-checker/texts/constituicao.txt")
#elapsed = time() - start_time
#print("{}".format(str(elapsed)))

#sample_file("D:\igor\OneDrive\Documentos\GitHub\spell-checker\dictionaries\palavras.txt",
#			"D:\igor\OneDrive\Documentos\GitHub\spell-checker\dictionaries\palavras_sample1.txt")

#wrong_words = ct.check("./texts/A-Caravana-de-Veneza.txt")

#ct_wrong_words = ct.check("D:\igor\OneDrive\Documentos\GitHub\spell-checker\dictionaries\palavras_sample.txt")
#rt_wrong_words = rt.check("D:\igor\OneDrive\Documentos\GitHub\spell-checker\dictionaries\palavras_sample.txt")

#print("low_memory=True:",end="")
#start_time = time()
#ct = from_csv("D:\igor\OneDrive\Documentos\GitHub\spell-checker\palavras_sample.txt")
#low_memory_time = time() - start_time
#print(" {}".format(str(low_memory_time)))
#
#print("low_memory=False:",end="")
#start_time = time()
#ct = from_csv("D:\igor\OneDrive\Documentos\GitHub\spell-checker\palavras_sample.txt",False)
#no_low_memory_time = time() - start_time
#print(" {}".format(str(no_low_memory_time)))

#print("low_memory=True:",end="")
#start_time = time()
#for i in range(5):
#	print(i)
#	ct = from_csv("D:\igor\OneDrive\Documentos\GitHub\spell-checker\palavras_sample.txt")
#low_memory_time = (time() - start_time)/50

#print("low_memory=False:",end="")
#start_time = time()
#for i in range(5):
#	print(i)
#	ct = from_csv("D:\igor\OneDrive\Documentos\GitHub\spell-checker\palavras_sample.txt",False)
#no_low_memory_time = (time() - start_time)/50