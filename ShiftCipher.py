import string
def encrypt(message, key):
    
    cipher = dict()
    encrypted_message = ' '

    for letter, new_letter in enumerate(string.ascii_lowercase):
        cipher[new_letter] = string.ascii_lowercase[(letter+key)%26]

    for char in message:
        if char.islower():
            encrypted_message += cipher[char]
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, key):
    
    decoder = dict()
    decrypted_message = ' '

    for letter, new_letter in enumerate(string.ascii_lowercase):
        decoder[new_letter] = string.ascii_lowercase[(letter-key)%26]
    for char in message:
        if char.islower():
            decrypted_message += decoder[char]
        else:
            decrypted_message += char

    return decrypted_message
    
def main():
    print("welcome to the encryptor/decryptor zone")
    continue_prompt = "y"
    while continue_prompt == 'y':
        response = input("type E/e to encrypt or D/d to decrypt: ").lower()
        if response == 'e':
            message = [x for x in input("enter a message to encrypt: ").lower()]
            key = int(input("enter the encryption key: "))
            print(f"The encrypted message is {encrypt(message, key)}")
        else:
            message = [x for x in input("enter a message to decrypt: ").lower()]
            key = int(input("enter the encryption key: "))
            print(f"the decrypted message is {decrypt(message, key)}")
        
        continue_prompt = input("would you like to encrypt or decrypt another message? enter Y/y or N/n: ").lower()


main()
