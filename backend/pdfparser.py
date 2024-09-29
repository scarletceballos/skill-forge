import requests
import os

def parse_pdf(filepath):
	url = "https://api.affinda.com/v3/documents"
	with open(filepath, 'rb') as f:
		files = {'file': f}
		headers = {
		"Authorization": f"Bearer {os.getenv('AFFINDA_API_KEY')}",
		"accept": "application/json"
	}
	response = requests.post(url, files=files, headers=headers)
	print(response.json())
	return response.json()
# how is this different from the code that is in the Affinda documentation?
