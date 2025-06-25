from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

SECRET_KEY = b'ThisIsASecretKey'  # 16 bytes 고정 (누나가 변경 가능)

# AES 암호화 함수
def encrypt(plain_text):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return {'iv': iv, 'ciphertext': ct}

# AES 복호화 함수
def decrypt(encrypted_data):
    iv = base64.b64decode(encrypted_data['iv'])
    ct = base64.b64decode(encrypted_data['ciphertext'])
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')