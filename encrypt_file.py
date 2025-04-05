from cryptography.fernet import Fernet

def load_key():
    with open("fernet.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    with open(file_path + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File encrypted and saved as: {file_path}.encrypted")

if __name__ == "__main__":
    path = input("Enter file path to encrypt: ")
    encrypt_file(path)
