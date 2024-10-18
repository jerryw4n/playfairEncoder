# Playfair Cipher Encoder

This project is a Python script that encrypts messages using the Playfair cipher. Users provide a plaintext message and a key, and the script outputs the encrypted message.

## Features
- **Key Matrix Creation**: Generates a 5x5 matrix from the provided key, removing duplicates and treating 'i' and 'j' as the same letter.
- **Letter Replacement**: Replaces 'j' with 'i' and adds padding characters 'x' or 'q' where necessary.
- **Pair Encryption**: Encrypts pairs of letters according to the Playfair cipher rules.
- **Full Encryption Process**: Combines all functions to output the final ciphertext.
