from xor_cipher import XORCipher  # Import the XORCipher class

def main():
    # Read keys from files
    with open("key1.txt", "r") as f:
        key1 = f.read().strip()
    
    with open("key2.txt", "r") as f:
        key2 = f.read().strip()

    # Create an instance of XORCipher
    cipher = XORCipher(key1, key2)
    
    # Read the ciphertext from the file
    with open("ciphertext.txt", "r") as f:
        ciphertext = f.read()

    # Decrypt
    decrypted_text = cipher.double_decrypt(ciphertext)
    print(f"Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
