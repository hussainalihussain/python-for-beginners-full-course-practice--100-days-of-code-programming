import requests

url = "https://www.w3schools.com/python"


response = requests.get(url)

print(response.text)