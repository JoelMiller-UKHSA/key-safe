from key_safe.encryption import encrypt, decrypt


def test_encrypt_decrypt() -> None:
    plaintext_in = "secret message"
    test_key = "badpass"

    ciphertext = encrypt(plaintext_in, test_key)
    plaintext_out = decrypt(ciphertext, test_key)

    assert plaintext_in == plaintext_out
