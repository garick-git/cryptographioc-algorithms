# Garick Mendez - St. Edward's University

def main():
    # setting an initial value of 0 to open up while loop
    selectedFunction = 0
    while selectedFunction != 3:
        try:
            selectedFunction = int(input("\nWhich function do you want?\n1. One Time Pad\n2. RC4\n3. Exit\n"))
        except EOFError:
            print("Input stream closed. Exiting program.")
            break

        if selectedFunction == 1: # one time pad selection
            plaintext = input('Your plaintext --> ')
            key = keyToByte(adjustKey(input('Your key --> '), len(plaintext)))

            # encrypting the plaintext
            encrypted_text = oneTimePad(plaintext, key)
            # decrypting the plaintext
            decrypted_text = decryptOTP(encrypted_text, key)

            # displaying the results
            print('The ciphertext is:', ''.join([byte.decode('latin-1') for byte in encrypted_text]))
            print('Decrypted ciphertext:', decrypted_text)
            
        elif selectedFunction == 2: # RC4 selection
            plaintext = input('Your plaintext --> ')
            key = input('Your key --> ')
            keystream = rC4(plaintext, key)
            # encrypting 
            encrypted_text = oneTimePad(plaintext, keystream)
            # decrypting 
            decrypted_text = decryptRC4(encrypted_text, keystream)

            # Display results
            print('The ciphertext is:', ''.join([byte.decode('latin-1') for byte in encrypted_text]))
            print('Decrypted text:', decrypted_text)
            
        elif selectedFunction == 3: # exit program
            print('Thanks! Exiting program.\n')
            break

        else:
            print('Invalid option. Please select again.\n')

# 1. oneTimePad()
def oneTimePad(plaintext, keystream):
    ciphertext = []
    for i in range(len(plaintext)):
        # Convert plaintext and keystream bytes to integers for XOR operation
        plaintext_byte = ord(plaintext[i])
        keystream_byte = keystream[i]
        # Perform XOR operation between plaintext byte and keystream byte
        ciphertext_byte = plaintext_byte ^ keystream_byte
        # Convert the result back to a byte and append to ciphertext
        ciphertext.append(bytes([ciphertext_byte]))
    return ciphertext


# 2. rC4()
def rC4(plaintext, key):
    # adjusting the size of the key
    key = adjustKey(key, len(plaintext))

    # PHASE 1: Initialization
    s = []
    k = []
    for i in range(256):
        s.append(i)
        # this is appending the decimal of key[i]
        k.append(ord(key[i % len(key)]))

    j = 0
    for i in range(256):
        j = (j + s[i] + k[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]  # swap (s[i] with s[j])
    i = j = 0

    # PHASE 2: RC4 keystream gen.
    keystream = []
    for _ in range(len(plaintext)):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]  # swap (s[i], s[j])
        t = (s[i] + s[j]) % 256
        keystream_byte = s[t]

        # appending the keystream with byte values in each index
        keystream.append(keystream_byte)

    return keystream


# --- HELPER FUNCTIONS ---

# Function to extend key and prepare it for oneTimePad()
def adjustKey(key, desiredLength):
    adjustedKey = ""
    if len(key) == desiredLength:
        return key
        
    # extending the key
    elif len(key) < desiredLength:
        keyRepetitions = desiredLength // len(key)
        charCount = desiredLength % len(key)
        adjustedKey = key * keyRepetitions
        adjustedKey += adjustedKey[:charCount]
        
    # truncating the key
    else:
        adjustedKey = key[:desiredLength]
    
    # Convert list of integers to a string
    adjustedKey = ''.join(map(str, adjustedKey))  # Join the map object into a single string

    print("The adjusted key:", adjustedKey)
    return adjustedKey

def decryptOTP(ciphertext, key):
    # converting hexadecimal ciphertext to ASCII 
    plaintext = b''
    for i in range(len(ciphertext)):
        # Convert each ciphertext byte to ASCII
        ciphertext_ascii = ciphertext[i].decode('utf-8')
        
        # Perform XOR operation between ASCII values of ciphertext and key bytes
        xor_result = ord(ciphertext_ascii) ^ key[i]
        
        # Convert the result back to byte and append to plaintext
        plaintext += bytes([xor_result])
    
    return plaintext.decode('utf-8')

def decryptRC4(ciphertext, keystream):
    plaintext = ''
    for i in range(len(ciphertext)):
        xor_result = ord(ciphertext[i]) ^ keystream[i]  # Use ciphertext here
        plaintext += chr(xor_result)
    return plaintext

# I used AI to help me generate the following two functions:
def plaintextToByte(plaintext):
    bytePlainText = plaintext.encode('utf-8')
    return bytePlainText

def keyToByte(key):
    byteKey = key.encode('utf-8')
    return byteKey

main()