import json
from bill_fetch_api import query_bill_fetch_api
from bill_pay_api import query_bill_pay_api
from utility_functions import encrypt_request_payload, decrypt_api_response, generate_checksum


user_input = '{"data": {"loan_number":"BAS123JKE"},"checksum": "4406f3578082e33d1b16c0a7da74d2eb921eab48"}'
fetch_request_payload = json.loads(user_input)
checksum_data = fetch_request_payload["data"]
checksum_string = json.dumps(checksum_data)
fetch_request_payload["checksum"] = generate_checksum(checksum_string)
fetch_request_payload = json.dumps(fetch_request_payload)
encrypted_payload = encrypt_request_payload(fetch_request_payload)
fetch_response = query_bill_fetch_api(encrypted_payload)
plaintext_response = decrypt_api_response(fetch_response)

print("BILL FETCH API REQUEST RESPONSE DATA ")
print("Encrypted request payload is ", encrypted_payload)
print("==============================")
print("Encrypted response is ", fetch_response)
print("===============================")
print("Decrypted response is ", plaintext_response)
print("==================")


user_input = '{"data": {"loan_number":"BAS123JKE", "fetchId": "37797773", "amountPaid":"2000", "txnRefId":"12312asD"},"checksum": "e9b17c190f20147e19c52cf9b32ad78b2069c0db"}'
pay_request_payload = json.loads(user_input)
fetch_bill_response = json.loads(plaintext_response)
fetchId = fetch_bill_response["details"]["fetchId"]
pay_request_payload["data"]["fetchId"] = fetchId
checksum_data = pay_request_payload["data"]
checksum_string = json.dumps(checksum_data)
pay_request_payload["checksum"] = generate_checksum(checksum_string)
pay_request_payload = json.dumps(pay_request_payload)
encrypted_payload = encrypt_request_payload(pay_request_payload)
pay_response = query_bill_pay_api(encrypted_payload)

print("BILL PAY API REQUEST RESPONSE")
plaintext_response = decrypt_api_response(pay_response)
print("Encrypted request payload is ", encrypted_payload)
print("==============================")
print("Encrypted response is ", pay_response)
print("===============================")
print("Decrypted response is ", plaintext_response)
print("==================")