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

	if response.status_code != 200:
		print("Error parsing PDF: ", response.json())
		return None
	print(response.json())
	return response.json()
# how is this different from the code that is in the Affinda documentation?
 
def fetch_topic_summary(topic):
	url = f"https://api.duckduckgo.com/?q={topic}&format=json&no_redirect=1&no_html=1"
	response = requests.get(url)
	data = response.json()

	if 'Abstract' in data and data['Abstract']:
		return data['Abstract']
	else:
		return "No summary found."



`
