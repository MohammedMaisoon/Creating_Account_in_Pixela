import requests

pixela_endpoint = "YOUR ENDPOINT"
TOKEN = "YOUR TOKEN"
USERNAME = "YOUR USERNAME"
graph_id = "YOUR ID"
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

response = requests.post(url=pixela_endpoint,json=user_params)
print(response.text)
