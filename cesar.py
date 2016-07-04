"""
easy chiffrement
"""

import string


def break_cesar(text):
	"""
	The not very smart way
	"""
	alphabet = list(string.ascii_uppercase)
	for key in xrange(1, 26):
		text_decode = ""
		for elt in text:
			if elt.isalpha():
				elt_index = 0
				alpha_index = 0
				decode_index = 0
				for letter in alphabet:
					if(letter == elt):
						elt_index = alpha_index
						decode_index = (elt_index + key) % 26
						text_decode = text_decode + alphabet[decode_index]
					alpha_index = alpha_index + 1
			else:
				text_decode = text_decode + elt
		print text_decode + "[ "+str(key)+" ]"



def encode_cesar(text, key):
	"""
	ecrit a l'arrache
	"""
	text_encode = ""
	alphabet = list(string.ascii_uppercase)
	for elt in text:
		if elt.isalpha():
			elt_index = 0
			alpha_index = 0
			encode_index = 0
			for letter in alphabet:
				if(letter == elt):
					elt_index = alpha_index
					encode_index = (elt_index + key) % 26
					text_encode = text_encode + alphabet[encode_index]
				alpha_index = alpha_index + 1
		else:
			text_encode = text_encode + elt
	return text_encode


"""
TEST SPACE
"""


text_encode = encode_cesar("TARTIFLETTE", 5)
break_cesar(text_encode)
