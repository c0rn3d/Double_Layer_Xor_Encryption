from xor_cipher import XORCipher  # Import the XORCipher class

def main():
    # Read keys from files
    with open("key1.txt", "r") as f:
        key1 = f.read().strip()
    
    with open("key2.txt", "r") as f:
        key2 = f.read().strip()

    # Create an instance of XORCipher
    cipher = XORCipher(key1, key2)
    
    # Encrypt
    plaintext = input("Enter the plaintext: ")
    ciphertext = cipher.double_encrypt(plaintext)
    print(f"Ciphertext: {ciphertext}")
    
    # Save the ciphertext to a file
    with open("ciphertext.txt", "w") as f:
        f.write(ciphertext)

if __name__ == "__main__":
    main()
