from cryptography.exceptions import InvalidSignature  # Import InvalidSignature exception

# Rest of your code remains the same...

# Verify signature with intentionally modified data_to_sign
modified_data_to_sign = b"Modified data"  # Change the data
try:
    public_key.verify(
        signature,
        modified_data_to_sign,  # Use modified data for verification
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature verification successful")
except InvalidSignature:
    print("Invalid signature: Signature verification failed")