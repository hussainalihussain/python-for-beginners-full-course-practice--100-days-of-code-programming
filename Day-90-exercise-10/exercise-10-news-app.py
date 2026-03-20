import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

# GET https://newsapi.org/v2/top-headlines?country=us&apiKey=NEWS_API_KEY
token = os.getenv('NEWS_API_KEY')

def print_options(label, options):
  print(f"{label}:")

  serial_number = 1

  is_dictionary = type(options) == type({})

  for option in options:
    label = options[option].capitalize() if is_dictionary else option.capitalize()
    sn = option if is_dictionary else serial_number
    print(f"{sn}. {label}")

    serial_number+=1
  
  print()

def get_news(country, category):
  if not country or not category:
    return []

  limit = 5
  url = "https://newsapi.org/v2/top-headlines?"
  url += f"apiKey={token}"
  url += f"&pageSize={limit}"
  url += f"&country={country}"
  url += f"&category={category}"

  response = requests.get(url)

  # copied from chatgpt
  response_dict = response.json()

  # ✅ Check for errors - copied from chatgpt
  if response.status_code != 200:
    print("API Error:", response_dict.get("message"))

    return []

  # copied from chatgpt
  if "articles" not in response_dict:
    print("No articles found!")

    return []

  return response_dict['articles']

def print_news(news):
  print()
  print(f"Title: {news['title']}")
  print(f"Source: {news['source']['name']}")
  print(f"Publish At: {news['publishedAt']}")
  print()


categories = [
  "technology",
  "business",
  "entertainment",
  "health",
  "sports",
]
countries = {
  "us": "United States",
  "pk": "Pakistan",
  "in": "India"
}

running = True

while running:
  try:
    print_options("Available categories", categories)
    category = int(input("Choose 1-5 for category: "))

    print_options("Available countries (choose us to get non empty response)", countries)
    country = input("Choose one of the country: ")

    news = get_news(country, categories[category - 1])

    for single_news in news:
      print_news(single_news)

    running = False
  except ValueError as e:
    print("##################")
    print("# Invalid Input! #")
    print("##################")
    print(e)
    running = True
  except Exception as e:
    running = False
    print("Error:", e)