#!/usr/bin/python
import random

arquivo_palavras = open("palavras.txt", "r")
palavras = arquivo_palavras.read().split("\n")
randomico = random.randint(0, len(palavras)-1)
print('Palavra sorteada: ' +  palavras[randomico])
arquivo_palavras.close()
