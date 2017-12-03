from Crypto.Cipher import AES
import base64, os

msg_text = b'gurukul123'
secret_key = b'1234567890123456' # create new & store somewhere safe

cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
encoded = base64.b64encode(cipher.encrypt(msg_text))
# ...
decoded = cipher.decrypt(base64.b64decode(encoded))
print(decoded.strip())

def encryption(privateInfo):
	#32 bytes = 256 bits
	#16 = 128 bits
	# the block size for cipher obj, can be 16 24 or 32. 16 matches 128 bit.
	BLOCK_SIZE = 16
	# the character used for padding
	# used to ensure that your value is always a multiple of BLOCK_SIZE
	PADDING = '{'
	# function to pad the functions. Lambda
	# is used for abstraction of functions.
	# basically, its a function, and you define it, followed by the param
	# followed by a colon,
	# ex = lambda x: x+5
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	# encrypt with AES, encode with base64
	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
	# generate a randomized secret key with urandom
	secret = os.urandom(BLOCK_SIZE)
	print('encryption key:',secret)
	# creates the cipher obj using the key
	cipher = AES.new(secret, AES.MODE_ECB)
	# encodes you private info!
	encoded = EncodeAES(cipher, privateInfo)
	print('Encrypted string:', encoded)

def decryption(encryptedString):
	PADDING = '{'
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	#Key is FROM the printout of 'secret' in encryption
	#below is the encryption.
	encryption = encryptedString
	key = ''
	cipher = AES.new(key)
	decoded = DecodeAES(cipher, encryption)
	print(decoded)