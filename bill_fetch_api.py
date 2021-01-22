import base64
import json
import uuid
import hashlib
import datetime
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad




def query_bill_fetch_api(payload):
    response = None
    utc_datetime = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    date = datetime.date.today().strftime("%Y%m%d")
    api_key = str(uuid.uuid4())
    request_url = 'https://4hfvpey3dk.execute-api.ap-south-1.amazonaws.com/v1/bill-apis/stage/modules/module/bbps/bills/fetch'
    auth_headers = {"Authorization": f"AES-256 X-API-Key={api_key} Credential=1324/{date} SignedHeaders=content-type;host;x-amz-date, Signature=setu", "X-Amz-Date": utc_datetime}
    r=requests.post(request_url, data=payload,headers=auth_headers)
    if r.status_code == 200:
        response = r.text
    return response

