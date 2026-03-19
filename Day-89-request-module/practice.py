import requests
from bs4 import BeautifulSoup

url = "https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start"


response = requests.get(url).text

soap = BeautifulSoup(response, 'html.parser')

print(f"All h1 inside {url} are:")

for h1 in soap.find_all('h1'):
    print(h1)