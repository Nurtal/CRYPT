# -*- coding: utf-8 -*-
##
## -> script to encrypt and decrypt a txt file
## -> use vigenere
## -> take 3 arguments:
## 	- action :
##		- encrypt
##		- decrypt
## 	- key
##	- filename
## 

import sys

instruction = str(sys.argv[1])
clef = str(sys.argv[2])
target_file = str(sys.argv[3])

## encrypt captainlog.md
if(instruction == "encrypt"):
	
	# lecture du fichier messageclair.txt
	fichier=open(target_file,"r")
	texteclair=fichier.read()
	fichier.close()
	
	# initialisation du texte chiffre
	textechiffre=""

	# chiffrement
	for i in range (0,len(texteclair)):
		
		caractere=texteclair[i]
		code=ord(caractere)
		decalage=ord(clef[i%len(clef)])
		codechiffre=(code+decalage)%256
		caracterechiffre=chr(codechiffre)
		textechiffre=textechiffre+caracterechiffre

	# ecriture dans le fichier messagechiffre.txt
	fichier=open(target_file,"w")
	fichier.write(textechiffre)
	fichier.close()

## decrypt captainlog.md
elif(instruction == "decrypt"):
	
	# lecture du fichier messagechiffre.txt
	fichier=open(target_file,"r")
	textechiffre=fichier.read()
	fichier.close()

	# initialisation du texte clair
	texteclair=""

	# dechiffrement
	for i in range (0,len(textechiffre)):
		caractere=textechiffre[i]
		code=ord(caractere)
		decalage=ord(clef[i%len(clef)])
		codeclair=(code-decalage)%256
		caractereclair=chr(codeclair)
		texteclair=texteclair+caractereclair

	# ecriture dans le fichier messageclair.txt
	fichier=open(target_file,"w")
	fichier.write(texteclair)
	fichier.close()

else:

	print "[ERROR] => wrong instruction"