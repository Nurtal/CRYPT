"""
python 2
"""


from Crypto.Cipher import Blowfish


INPUT_SIZE = 8

def pad_string(str):
	"""
	encrypt string
	"""
	new_str = str
	pad_chars = INPUT_SIZE - (len(str) % INPUT_SIZE)
	if pad_chars != 0:
		for x in range(pad_chars):
			new_str += " "
	return new_str



def encryptFile(key, fileName):
	"""
	encrypt text in fileName using
	Blowfish algorithm. write a new
	file with encrypted data (filename_encrypted)
	-> key is a string
	-> fileName is a string
	"""

	plaintext = ""
	dataToEncrypt = open(fileName, "r")
	for line in dataToEncrypt:
		plaintext = plaintext + line
	dataToEncrypt.close()

	crypt_obj = Blowfish.new(key, Blowfish.MODE_ECB)
	ciphertext = crypt_obj.encrypt(pad_string(plaintext))

	fileNameInArray = fileName.split(".")
	encryptedFileName = fileNameInArray[0]+"_encrypted."+fileNameInArray[1]

	encryptedFile = open(encryptedFileName, "w")
	encryptedFile.write(ciphertext)
	encryptedFile.close()



def decryptFile(key, fileName):
	"""
	decrypt text in fileName using
	Blowfish algorithm. write a new file 
	with clair data.
	-> key is a string
	-> fileName is a string
	"""

	ciphertext = ""
	encryptedFile = open(fileName, "r")
	for line in encryptedFile:
		ciphertext = ciphertext + line
	encryptedFile.close()

	crypt_obj = Blowfish.new(key, Blowfish.MODE_ECB)
	plainText = crypt_obj.decrypt(ciphertext)

	fileNameInArray = fileName.split("_encrypted.")
	newFileName = fileNameInArray[0]+"."+fileNameInArray[1]

	newFile = open(newFileName, "w")
	newFile.write(plainText)
	newFile.close()


encryptFile("RAFGH","test.py")
decryptFile("RAFGH", "test_encrypted.py")