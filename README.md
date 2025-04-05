# Secure-File-Encryption-and-Decryption-with-Fernet-Key
# 🔐 Secure File Encryption & Decryption using Python (Fernet)

A simple yet effective Python-based tool to encrypt and decrypt files securely using symmetric key cryptography (Fernet) from the `cryptography` library. Designed to demonstrate real-world file protection practices.

## 📁 Features

- Symmetric encryption and decryption using Fernet (AES-128 under the hood)
- Secure key generation and local storage
- Command-line interface (CLI) for ease of use
- Tested on `.txt` and other binary file formats

## 🔧 Requirements

- Python 3.6+
- `cryptography` library

Install dependencies:
pip install cryptography
---------------------------------------------------------------------------------------
Step 1. Generate Encryption Key
Creates a fernet.key file used for both encryption and decryption.
python generate_key.py

Step 2. Encrypt a File
Encrypt any file (text, PDF, etc.)
python encrypt_file.py
📥 Enter the full path of the file when prompted.
Output: A new file with .encrypted extension.

3. Decrypt a File
Decrypt any .encrypted file using the saved key.
python decrypt_file.py
📥 Enter the full path of the encrypted file when prompted.
Output: A new file with .decrypted extension.
------------------------------------------------------------------------------------------
⚠️ Security Note
Keep your fernet.key file safe and never share it.
If the key is lost or compromised, the encrypted files cannot be recovered.
For added security, consider storing the key using environment variables or a key vault.



