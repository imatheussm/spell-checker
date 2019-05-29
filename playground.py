from os import getcwd
from sys import path as sys_path
#from time import time
sys_path.append(getcwd())
from spell_checker import *

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

print(", ".join([character.character for character in ct.next_characters]))

#print("\n\n")


#print("Comparing execution times:")

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