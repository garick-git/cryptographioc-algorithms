# Garick Mendez - St. Edward's University

# OPTION 1
def encription():
    print("\nStarting encryption")
    n = int(input("Key value n = "))

    # If n is an int equal to or greater than 0, continue
    if n < 0:
        print('Integer has to be >= 0')
        encription()
    else:
        with open("plaintext.txt", "r") as f:
            plaintext = f.read()

    special_characters = r'\.[]{}()<>*+-=!?^$|,\' '

    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        elif char in special_characters:
            char_index = (special_characters.index(char) + n) % len(special_characters)
            encrypted_text += special_characters[char_index]
        else:
            encrypted_text += char

    with open("ciphertext.txt", "w") as f:
        f.write(encrypted_text)

    print("\nEncryption completed! Here is the encrypted message:")
    print(encrypted_text)

# OPTION 2
def decription():
    print("\nStarting decryption")
    n = int(input("Key value n = "))
    if n < 0:
        print('Integer has to be >= 0')
        decription()
    else:
        with open("ciphertext.txt", "r") as f:
            ciphertext = f.read()
        plain_text = ""
        special_characters = r'\.[]{}()<>*+-=!?^$|,\' '

        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    # (-n) since we are reversing the encryption
                    plain_text += chr((ord(char) - ord('a') - n) % 26 + ord('a'))
                else:
                    plain_text += chr((ord(char) - ord('A') - n) % 26 + ord('A'))
            elif char in special_characters:
                char_index = (special_characters.index(char) - n) % len(special_characters)
                plain_text += special_characters[char_index]
            else:
                plain_text += char

        with open("plaintext.txt", "w") as f:
            f.write(plain_text)

        print("\nDecryption completed! Here is the decrypted message:")
        print(plain_text)


# OPTION 3
def break_function():
    print("\nBreak option selected. This is the cipher text:")
    with open("ciphertext.txt", "r") as f:
        ciphertext = f.read()
    print(ciphertext)

    n = int(input("\nEnter an N value to decrypt the message: "))
    if n < 0:
        print('Integer has to be >= 0')
        break_function()
    else:
        special_characters = r'\.[]{}()<>*+-=!?^$|,\' '

        with open("ciphertext.txt", "r") as f:
            ciphertext = f.read()
        plain_text = ""
        for char in ciphertext:
            if char.isalpha():
                if char.islower():
                    plain_text += chr((ord(char) - ord('a') - n) % 26 + ord('a'))
                else:
                    plain_text += chr((ord(char) - ord('A') - n) % 26 + ord('A'))
            elif char in special_characters:
                char_index = (special_characters.index(char) - n) % len(special_characters)
                plain_text += special_characters[char_index]
            else:
                plain_text += char

        with open("plaintext.txt", "w") as f:
            f.write(plain_text)
        print('\nDecryption completed! Here is the decrypted message:')
        print(plain_text)

        correctMessage = input("Was this the correct decrypted message? (Y/N): ").strip().upper()
        if correctMessage == 'Y' or correctMessage == 'y':
            print(f'Great! The key was {n}.')
        else:
            # restart program if the key wasn't correctly input
            break_function()

def option_4():
    print("Exiting program")
    exit()

while True:
    try:
        user_input = int(input("\n1 - Encrypt \n2 - Decrypt \n3 - Break \n4 - Exit\nYour choice: "))
        if 1 <= user_input <= 3:
            if user_input == 1:
                encription()
            elif user_input == 2:
                decription()
            elif user_input == 3:
                break_function()
        elif user_input == 4:
            option_4()
        else:
            print("\nInvalid input. Please enter a number between 1 and 4.")
    except ValueError:
        print("\nInvalid input. Please enter a valid number.")