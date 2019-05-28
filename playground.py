from os import getcwd
from sys import path as sys_path
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