import os

def generate_random_key(length):
    return os.urandom(length).decode('latin1')  # latin1 encoding to handle non-printable bytes

def main():
    length = int(input("Enter the length for the keys: "))
    
    key1 = generate_random_key(length)
    key2 = generate_random_key(length)
    
    print(f"Generated Key 1: {key1}")
    print(f"Generated Key 2: {key2}")
    
    # Optionally, save keys to files
    with open("key1.txt", "w") as f:
        f.write(key1)
    
    with open("key2.txt", "w") as f:
        f.write(key2)

if __name__ == "__main__":
    main()
