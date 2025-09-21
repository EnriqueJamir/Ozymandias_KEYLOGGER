import os
from crypto_storage import decrypt_data

def analyze_logs(storage_dir, key):
    reports = []
    for file in os.listdir(storage_dir):
        if file.endswith(".bin"):
            with open(os.path.join(storage_dir, file), 'rb') as f:
                content = f.read()
                nonce, ciphertext, tag = content[:16], content[16:-16], content[-16:]
                try:
                    decrypted = decrypt_data(nonce, ciphertext, tag, key)
                    reports.append(decrypted)
                except:
                    continue
    return reports