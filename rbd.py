# import necessary libraries
from cryptography.fernet import Fernet
import hashlib

# define the encryption key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# define the data to be encrypted and encrypted data storage
logistics_data = {'id': '001', 'product': 'electronics', 'quantity': '10', 'price': '500'}
encrypted_data = {}

# encrypt the data
for key, value in logistics_data.items():
    message = value.encode()
    encrypted_data[key] = cipher_suite.encrypt(message)

# define the hash function
def hash_function(data):
    hash_object = hashlib.sha256(data)
    return hash_object.hexdigest()

# hash the encrypted data
hashed_data = {}
for key, value in encrypted_data.items():
    message = value.decode()
    hashed_data[key] = hash_function(message.encode())

# define the search function
def search_function(keyword):
    for key, value in hashed_data.items():
        if keyword in value:
            print(key + ": " + cipher_suite.decrypt(encrypted_data[key]).decode())

# example search query
search_function('0aa')