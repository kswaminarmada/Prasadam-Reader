from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def SetKey(Key):
    data = Key.encode() #bytearray(msg.encode('utf-8'))
    key = b'gurukul@12345678' #get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    file_out = open("Key.key", "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    
def GetKey():
    file_in = open("Key.key", "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    key = b'gurukul@12345678'
    # let's assume that the key is somehow available again
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data.decode()