from pydoc import plaintext

alphabets = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(alphabets)

def encrypt(plaintext, key):#encryption function
    cyphertext = ''
    for letter in plaintext:#go through each letter in the alphabet
        letter = letter.lower()#covert all letters to lowercase
        if not letter == ' ':
            index = alphabets.find(letter)
            if index == -1:
                cyphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                cyphertext += alphabets[new_index]
    return cyphertext

def decrypt(cyphertext, key):#decryption function
    plaintext = ''
    for letter in cyphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = alphabets.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                plaintext += alphabets[new_index]
    return plaintext


print()
print("*** CAESAR CYPHER PROGRAM ***")
print()

print('Do you want to Encrypt or Decrypt?')
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('Encryption Mode Selected...')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to Encrypt: ')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT: {ciphertext}')

elif user_input == 'd':
    print('Decryption Mode Selected...')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to Decrypt: ')
    plaintext = decrypt(text, key)
    print(f'PLAINTEXT: {plaintext}')
