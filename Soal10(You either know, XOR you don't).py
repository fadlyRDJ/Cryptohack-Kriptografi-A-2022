from pwn import xor

raw = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
flag_pattern = "crypto{"

encoded = bytes.fromhex(raw)

print(xor(flag_pattern.encode(), encoded))

guessed_key = "myXORkey"
print(xor(guessed_key.encode(), encoded))
