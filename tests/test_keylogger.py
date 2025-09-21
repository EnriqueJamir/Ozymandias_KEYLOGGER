"""
Testes unitários simulados para o Keylogger Ozymandias.
Todos os testes devem ser feitos em ambiente seguro.
"""

from src.keylogger_core import on_press, capture_clipboard
from src.parser import parse_input
from src.crypto_storage import encrypt_data, decrypt_data

def test_buffer_parsing():
    test_data = "senha123\nadmin456"
    parsed = parse_input(test_data)
    assert "senha123" in parsed
    assert "admin456" in parsed

def test_encryption_cycle():
    key = "1234567890123456"
    data = "teste de log"
    nonce, ciphertext, tag = encrypt_data(data, key)
    decrypted = decrypt_data(nonce, ciphertext, tag, key)
    assert decrypted == data