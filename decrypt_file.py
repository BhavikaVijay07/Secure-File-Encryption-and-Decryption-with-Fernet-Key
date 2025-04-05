from cryptography.fernet import Fernet
import os

def load_key():
    with open("fernet.key", "rb") as key_file:
        return key_file.read()

def decrypt_file(encrypted_path):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    original_file_path = encrypted_path.replace(".encrypted", ".decrypted")

    with open(original_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"File decrypted and saved as: {original_file_path}")

if __name__ == "__main__":
    path = input("Enter encrypted file path to decrypt: ")
    decrypt_file(path)
