from fastapi import FastAPI
from firebase import Firebase


config = {
    "apiKey": "AIzaSyBiM7pShglQoWESauwAhsmnDFYzFrBwj3k",
    "authDomain": "testing-with-fastapi.firebaseapp.com",
    "projectId": "testing-with-fastapi",
    "storageBucket": "testing-with-fastapi.appspot.com",
    "messagingSenderId": "117877501282",
    "appId": "1:117877501282:web:b7916553b4c2d24cf8503b",
    "measurementId": "G-JLPNZ0GLGC",
    "databaseURL": ""
}

# config = {

# }

firebase = Firebase(config)
auth = firebase.auth()

app = FastAPI()


@app.get("/")
def read_root():
    user = auth.sign_in_with_email_and_password("mfarzamalam@gmail.com", "123456")
    token_auth = auth.get_account_info(user.get('idToken'))
    return {"token_auth": token_auth}



# pip install firebase==3.0.0
# pip install python_jwt
# pip install sseclient
# pip install pycryptodome
# pip install requests-toolbelt
# token
# eyJhbGciOiJSUzI1NiIsImtpZCI6ImNlOWI4ODBmODE4MmRkYTU1N2Y3YzcwZTIwZTRlMzcwZTNkMTI3NDciLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vdGVzdGluZy13aXRoLWZhc3RhcGkiLCJhdWQiOiJ0ZXN0aW5nLXdpdGgtZmFzdGFwaSIsImF1dGhfdGltZSI6MTY3MjY0NjM0NywidXNlcl9pZCI6InlkS01OdEh2WFFQa0xWRHNTV3lnTFhLTzdXRjMiLCJzdWIiOiJ5ZEtNTnRIdlhRUGtMVkRzU1d5Z0xYS083V0YzIiwiaWF0IjoxNjcyNjQ2MzQ3LCJleHAiOjE2NzI2NDk5NDcsImVtYWlsIjoibWZhcnphbWFsYW1AZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbIm1mYXJ6YW1hbGFtQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.HopUtnKeDssvtwIqZq-rQmkXZQKuKozN46lgwhHS0cgSxfcH2qXRBYcX3-KpdlmbeIQi4CLuzIJxNExvf-V73FpUd1GLxZeh1MEocaIUvpS7uIOJ9kiMfnUeA5X0ES7VkFMiJ5IH4ddHNAjw6Qr1UGrqC_F8rPqZQUE-H6KT5dCR2KtTWQ48Orf9KMSxyfKOncogbKUpXw1n5Dvakouf7kAdDrRGMyrEwxrK59Ug8UYfc21F3xemuZZGo54VfiBYta17eIcLD6qETNIESlElQf8dGP88wRK4xfFn3MPGzhm6KNh-XUWW2LhEcZBvWb7tjJfl-h5f_vg7ZsG6H57mfg
