import secrets
from hashlib import sha256

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


SALT_LENGTH = 32


def encrypt(plaintext: str, password: str) -> str:
    salt = secrets.token_bytes(SALT_LENGTH)
    key = sha256(password.encode()).digest()
    ciphertext = salt + AESGCM(key).encrypt(salt, plaintext.encode(), None)
    return ciphertext


def decrypt(ciphertext: bytes, password: str) -> str:
    key = sha256(password.encode()).digest()
    plaintext = AESGCM(key).decrypt(
        ciphertext[:SALT_LENGTH], ciphertext[SALT_LENGTH:], None
    )
    return plaintext.decode()
