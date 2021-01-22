import base64
import json
import hashlib
import datetime
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad



def query_bill_pay_api(request):
    response = None
    utc_datetime = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    date = datetime.date.today().strftime("%Y%m%d")
    request_url = 'https://4hfvpey3dk.execute-api.ap-south-1.amazonaws.com/v1/bill-apis/stage/modules/module/bbps/bills/receipt'
    auth_headers = {"Authorization":f"AES-256 X-API-Key=f3aa13db-e5bf-4111-b5d3-e3404d2f2fe4 Credential=2256/{date}, SignedHeaders=content-type;host;x-amz-date, Signature=setu", "X-Amz-Date": utc_datetime}
    r=requests.post(request_url, data=request,headers=auth_headers)
    if r.status_code == 200:
        response = r.text
    return response

