from node.crypto.aes_util import encrypt, decrypt

def test_aes_encryption_decryption():
    key = b"1234567890123456"  # 16바이트 대칭키
    plaintext = b"secure mutual cloud transmission"

    ciphertext = encrypt(plaintext, key)
    decrypted = decrypt(ciphertext, key)

    assert decrypted == plaintext
