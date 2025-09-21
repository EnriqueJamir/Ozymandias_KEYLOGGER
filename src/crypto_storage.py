from Crypto.Cipher import AES
from hashlib import sha256
import os, json, time

storage_dir = "C:\\HacxLab\\secure_logs"
os.makedirs(storage_dir, exist_ok=True)

def encrypt_data(data, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return cipher.nonce, ciphertext, tag

def decrypt_data(nonce, ciphertext, tag, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')

def save_log(data, key, filename=None):
    if not filename:
        filename = f"log_{time.strftime('%Y%m%d_%H%M%S')}.bin"
    nonce, ciphertext, tag = encrypt_data(data, key)
    with open(os.path.join(storage_dir, filename), 'wb') as f:
        f.write(nonce + ciphertext + tag)