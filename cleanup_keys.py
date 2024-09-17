import os

def delete_keys():
    """
    Delete the key files (key1.txt and key2.txt) if they exist.
    """
    key1_path = "key1.txt"
    key2_path = "key2.txt"

    # Check if key1.txt exists and delete it
    if os.path.exists(key1_path):
        os.remove(key1_path)
        print(f"Deleted {key1_path}")
    else:
        print(f"{key1_path} not found")

    # Check if key2.txt exists and delete it
    if os.path.exists(key2_path):
        os.remove(key2_path)
        print(f"Deleted {key2_path}")
    else:
        print(f"{key2_path} not found")

if __name__ == "__main__":
    delete_keys()
