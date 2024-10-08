import random
import os

# Function to XOR encrypt the code
def xor_encrypt(code, key):
    encrypted_code = ""
    for i in range(len(code)):
        current_char = code[i]
        current_key = key[i % len(key)]
        encrypted_code += chr(ord(current_char) ^ ord(current_key))
    return encrypted_code

# Function to generate a random XOR key
def generate_key(length):
    key = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return key

# Encrypts the Python code from the input file
def encrypt_python_file(input_file, output_file):
    try:
        # Read the original Python code
        with open(input_file, 'r') as file:
            python_code = file.read()
        
        # Generate a key of sufficient length
        key_length = 100
        key = generate_key(key_length)
        
        # XOR encrypt the code
        encrypted_code = xor_encrypt(python_code, key)
        
        # Prepare obfuscated version with decryption logic
        obfuscated_code = f'''
import base64

# XOR decrypt function
def xor_decrypt(encrypted_code, key):
    decrypted_code = ""
    for i in range(len(encrypted_code)):
        decrypted_code += chr(ord(encrypted_code[i]) ^ ord(key[i % len(key)]))
    return decrypted_code

# Encrypted and obfuscated payload
encrypted_code = {repr(encrypted_code)}
key = "{key}"

# Decrypt and execute the code
decrypted_code = xor_decrypt(encrypted_code, key)
exec(decrypted_code)
'''

        # Write the obfuscated code to the output file
        with open(output_file, 'w') as obfuscated_file:
            obfuscated_file.write(obfuscated_code)
        
        print(f"[✔] Successfully encrypted and obfuscated the file: {output_file}")

    except FileNotFoundError:
        print(f"[X] Error: File {input_file} not found")

# Input and output files
input_file = input("[*] Enter the path of the Python file to encrypt: ")
output_file = input("[*] Enter the path to save the obfuscated file: ")

# Encrypt the Python code and save the obfuscated file
encrypt_python_file(input_file, output_file)
