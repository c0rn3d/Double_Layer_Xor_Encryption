class XORCipher:
    def __init__(self, key1, key2):
        """
        Initialize the XORCipher with two keys.
        :param key1: The first key used for encryption and decryption.
        :param key2: The second key used for encryption and decryption.
        """
        self.key1 = key1
        self.key2 = key2
    
    def xor_operation(self, data, key):
        """
        Perform XOR operation between data and key.
        :param data: The data to be XORed.
        :param key: The key used for XOR operation.
        :return: XORed result as a string.
        """
        # Repeat the key to match the data length
        key = self.repeat_key(key, len(data))
        
        # XOR each character of data with the corresponding character of the key
        return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(data, key))
    
    def repeat_key(self, key, length):
        """
        Repeat or truncate the key to match the given length.
        :param key: The original key.
        :param length: The desired length of the key.
        :return: A key of the specified length.
        """
        return (key * (length // len(key))) + key[:length % len(key)]

    def double_encrypt(self, plaintext):
        """
        Encrypt the plaintext using two keys.
        :param plaintext: The text to be encrypted.
        :return: Encrypted text.
        """
        # First layer of encryption with key1
        first_layer_encryption = self.xor_operation(plaintext, self.key1)
        
        # Second layer of encryption with key2
        second_layer_encryption = self.xor_operation(first_layer_encryption, self.key2)
        
        return second_layer_encryption

    def double_decrypt(self, ciphertext):
        """
        Decrypt the ciphertext using two keys.
        :param ciphertext: The text to be decrypted.
        :return: Decrypted text.
        """
        # First layer of decryption with key2
        first_layer_decryption = self.xor_operation(ciphertext, self.key2)
        
        # Second layer of decryption with key1
        plaintext = self.xor_operation(first_layer_decryption, self.key1)
        
        return plaintext
