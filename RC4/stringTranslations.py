# original string
string = "hello"
print('Our String:', string)

# string to char
charArray = []
for char in string:
    charArray.append(char)
print('Our char array:', charArray)

# char to ascii
chToAscii = []
for char in charArray:
	chToAscii.append(ord(char))
print('converted to ascii:', chToAscii)

# ascii to binary
# binary should be a string not an integer 
asToBinary = []
for asciiChar in chToAscii:
	asToBinary.append(bin(asciiChar)[2:])
print("now in binary:", asToBinary)

# binary to ascii
binToAscii = []
for binaryChar in asToBinary:
	binToAscii.append(int(binaryChar, 2))
print("back to ascii:", binToAscii)

# ascii to char
asToChar = []
for asciiChar in binToAscii:
	asToChar.append(chr(asciiChar))
print("now to char array:", asToChar)

# char to string
reconstructed_string = ''.join(asToChar)
print("Reconstructed string:", reconstructed_string)