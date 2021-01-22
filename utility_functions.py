import json
import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


string_key = 'assignmentToSetu'
bytes_key = string_key.encode('utf-8')
BLOCK_SIZE = 32


def generate_checksum(checksum_input):
    hash_object =  hashlib.sha1(str(checksum_input).encode("utf-8"))
    hash_value = hash_object.hexdigest()
    return hash_value


def encrypt_request_payload(data):
    byte_data = data.encode('utf-8')
    padded_bytes_data = pad(byte_data, BLOCK_SIZE)
    cipher = AES.new(bytes_key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(padded_bytes_data)
    base64_encoded_string = base64.b64encode(encrypted_data).decode('utf-8')
    return base64_encoded_string



def decrypt_api_response(response):
    bytes_response = base64.b64decode(response)
    cipher = AES.new(bytes_key, AES.MODE_ECB)
    response = cipher.decrypt(bytes_response)
    final_response = response.decode('utf-8')
    return final_response