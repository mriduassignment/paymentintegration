# paymentintegration
Bill Fetch API and Bill Pay API integration

The project is mistakenly pushed on master branch instead of main branch.

The project is an integration for Bill Fetch API and Bill Pay API. It consists of 4 files:

1. bill_fetch_api.py - consists of a function that makes HTTP request call to Bill fetch API. 
URL - https://4hfvpey3dk.execute-api.ap-south-1.amazonaws.com/v1/bill-apis/stage/modules/module/bbps/bills/fetch

2. bill_pay_api.py - consists of a function that makes HTTP request call to Bill Pay API.
URL - https://4hfvpey3dk.execute-api.ap-south-1.amazonaws.com/v1/bill-apis/stage/modules/module/bbps/bills/receipt

3. utility_functions.py - consists of functions called for generating checksum, encryption of request payload and decryption of response.

4. api_wrapper.py - makes call to functions present in the above 3 files.

5. requirements.txt - consists of all the required packages that need to be installed.
