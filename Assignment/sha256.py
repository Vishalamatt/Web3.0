from hashlib import sha256
from mimetypes import init
from time import time 

MAX = 1000000000
target = '00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

data = input("Enter data:")
init = time()
for x in range (MAX):
    s = data + str(x)
    if(SHA256(s) > sha256(bytes.fromhex(target)).hexdigest()):
        print (x-1)
        break
    
    else :
         x =  x + 1

print ("Time taken :", time() - init)