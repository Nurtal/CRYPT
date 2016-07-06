"""
chiffre de vigenere
test function
"""

def getComplementaryText(text, key):
	"""
	return complementary string for encoding
	"""

	index = 0
	text_2 = ""
	for letter in text:
		if(index < len(key)):
			text_2 = text_2 + key[index]
			index = index +1
		else:
			index = 0
			text_2 = text_2 + key[index]
			index = index + 1
	return text_2

def encodeChar(letter, letter_2):
	"""
	return encode char from vigenere table
	"""
	# Construction du carre de Vigenere
	Carre=[]
	ligne=[]
	for j in range(26):
		for i in range(26):
			ligne.append(chr(65+(i+j)%26))
    		Carre.append(ligne)
    		ligne=[]

	line_index = 0
	line_cmpt = 0
	for line in Carre:
		if (line[0] == letter):
			line_index = line_cmpt
		line_cmpt = line_cmpt + 1

	column_index = 0
	column_cmpt = 0
	for column in Carre[0]:
		if(column == letter_2):
			column_index = column_cmpt
		column_cmpt = column_cmpt + 1

	encodeChar = Carre[line_index][column_index]
	return encodeChar


def encodeString(text, key):
	"""
	encode string with vigenere chiffre
	"""

	text_2 = getComplementaryText(text, key)
	text_encode = ""
	index = 0
	for elt in text:
		encode_elt = encodeChar(elt, text_2[index])
		index = index + 1
		text_encode = text_encode + encode_elt

	return text_encode


"""
TEST SPACE
"""


print encodeString("LANGOUSTINE", "CHIEN")


