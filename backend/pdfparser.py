import requests

url = "https://api.affinda.com/v3/documents"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"wait\"\r\n\r\ntrue\r\n-----011000010111000001101001--"
headers = {
    "accept": "application/json",
    "content-type": "multipart/form-data; boundary=---011000010111000001101001"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)
