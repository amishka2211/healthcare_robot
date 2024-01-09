from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt data
data_to_encrypt = b"Sensitive health information"
encrypted_data = cipher_suite.encrypt(data_to_encrypt)
print("Encrypted data:", encrypted_data)