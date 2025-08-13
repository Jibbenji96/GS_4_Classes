def encode(text, key):
    cipher = make_cipher(key)
    ciphertext_chars = []
    
    for i in text:
        if i in cipher:
            ciphered_char = chr(65 + cipher.index(i))
            ciphertext_chars.append(ciphered_char)

    # print(ciphertext_chars)
    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)
    plaintext_chars = []
    # print(cipher)
    for i in encrypted:
        # print(abs(65 - ord(i)))
        plain_char = cipher[(abs(65 - ord(i)))]
        plaintext_chars.append(plain_char)

    # print(plaintext_chars)
    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(0, 26)]
    # print(alphabet)
    cipher_with_duplicates = list(key) + alphabet
    # print(cipher_with_duplicates)
    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher:
            cipher.append(cipher_with_duplicates[i])

    # print(cipher)
    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
