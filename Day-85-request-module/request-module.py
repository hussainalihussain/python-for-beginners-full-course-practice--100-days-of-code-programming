import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/python"

response = requests.get(url)

htmlResponse = response.text
# print(htmlResponse)

offlineHTML = html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<h2>Welcoming Section</h2>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,

<h2>Footer Area</h2>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soap = BeautifulSoup(htmlResponse, 'html.parser')

# print(soap.prettify())

for h2 in soap.find_all('h2'):
    print(h2)