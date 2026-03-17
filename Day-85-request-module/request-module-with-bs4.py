import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/python"

response = requests.get(url)

responseHtml = response.text

# print(responseHtml)

soap = BeautifulSoup(responseHtml, 'html.parser')

# print(soap.prettify())


h1Tags = soap.find_all('h1')

print("All h1 tags inside the page:")

for h1Tag in h1Tags:
    print(f"{h1Tag}")

print()


h2Tags = soap.find_all('h2')

print("All h2 tags inside the page:")

for h2Tag in h2Tags:
    print(f"{h2Tag}")