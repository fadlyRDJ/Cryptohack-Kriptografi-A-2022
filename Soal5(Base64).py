# import base64
from base64 import b64encode

# encode hex to bytes
hexstring = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
data = bytes.fromhex(hexstring)

# Using base64.b64encode() method
result = b64encode(data)
print(result)
