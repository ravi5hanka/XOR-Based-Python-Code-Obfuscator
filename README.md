How it works:

It reads the code from the specified input Python file.

The code is encrypted using the XOR operation with a randomly generated numeric key.

The encrypted code and the decryption logic (which includes the XOR key) are embedded into a new Python script that, when executed, decrypts and runs the original code.

The output file contains the obfuscated Python code, which can be executed to run the original program.

When the obfuscated script is executed, it decrypts the original code in memory and executes it using the exec() function. This helps protect the original code from being easily readable or altered.

Example Flow:
You input a Python file (e.g., my_script.py) to be encrypted.
The script generates a new file (e.g., obfuscated_script.py), which contains encrypted code and decryption logic.
Running obfuscated_script.py will execute the original logic after decrypting it in memory.

This program can be used to encrypt your python-based reverse shell codes, and it will help in evading the anti-virus solution.
