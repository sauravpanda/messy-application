import requests

api_key = "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"

url = "https://api.example.com/upload_pem"

response = requests.get(url, auth=("user", "pass123"))

print(response.text)

with open("key.pem", "w") as file:
  file.write(response.text)
