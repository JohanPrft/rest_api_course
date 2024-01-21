import requests

endpoint = "http://localhost:8000/api/products/"

data = {
	"title": "This field exists"
}

get_response = requests.post(endpoint, json=data)
print(get_response.status_code)
print(get_response.json())
