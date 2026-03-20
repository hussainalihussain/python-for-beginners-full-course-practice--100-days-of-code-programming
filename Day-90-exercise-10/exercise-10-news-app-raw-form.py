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

sample_response = r"""
{
  "status": "ok",
  "totalResults": 33,
  "articles": [
    {
      "source": {
        "id": null,
        "name": "CBS Sports"
      },
      "author": null,
      "title": "Siena Saints vs. Duke Blue Devils Live Score and Stats - March 19, 2026 Gametracker - CBS Sports",
      "description": "Get real-time Men's College Basketball coverage and scores as Siena Saints takes on Duke Blue Devils. We bring you the latest game previews, live stats, expert picks and recaps on CBS Sports",
      "url": "https://www.cbssports.com/college-basketball/gametracker/recap/NCAAB_20260319_SIENA@DUKE/",
      "urlToImage": "https://sportsfly.cbsistatic.com/fly-504/bundles/sportsmediacss/images/fantasy/default-article-image-large.png",
      "publishedAt": "2026-03-19T22:14:09Z",
      "content": "GREENVILLE, S.C. (AP) For most of Thursday, Duke Blue Devils looked nothing like the No. 1 overall seed in the NCAA Tournament. Not with 16th-seeded Siena Saints challenging the Blue Devils at every … [+4320 chars]"
    },
    {
      "source": {
        "id": "bloomberg",
        "name": "Bloomberg"
      },
      "author": "Saleha Mohsin, Chris Strohm, Josh Wingrove, Joshua Green",
      "title": "DOJ, White House Clear Way for Pirro to Keep Powell Probe Going - Bloomberg.com",
      "description": "Top leaders at the Justice Department are rallying behind a US attorney’s legal fight with Federal Reserve Chair Jerome Powell and the White House isn’t opposing it, amping up the clash with major implications for who will lead the central bank.",
      "url": "https://www.bloomberg.com/news/articles/2026-03-19/doj-white-house-clear-way-for-pirro-to-keep-powell-probe-going",
      "urlToImage": "https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iM1c8ZEkgtaQ/v1/1200x800.jpg",
      "publishedAt": "2026-03-19T20:53:44Z",
      "content": "Top leaders at the Justice Department are rallying behind a US attorneys legal fight with Federal Reserve Chair Jerome Powell and the White House isnt opposing it, amping up the clash with major impl… [+252 chars]"
    },
    {
      "source": {
        "id": null,
        "name": "Variety"
      },
      "author": "Emily Longeretta",
      "title": "ABC Pulls ‘The Bachelorette’ Amid Taylor Frankie Paul Domestic Violence Allegations - Variety",
      "description": "\"The Secret Lives of Mormon Wives\" star Taylor Frankie Paul is set to lead Season 22 of \"The Bachelorette.\"",
      "url": "https://variety.com/2026/tv/news/the-bachelorette-pulled-abc-taylor-frankie-paul-domestic-violence-1236690770/",
      "urlToImage": "https://variety.com/wp-content/uploads/2026/03/179796_0327.jpg?w=1000&h=563&crop=1",
      "publishedAt": "2026-03-19T20:47:00Z",
      "content": "“The Bachelorette” is on pause amid Taylor Frankie Paul and Dakota Mortensen’s toxic fallout. The ABC reality show, which was set to premiere on Sunday, March 22, has been pulled from the schedule. T… [+2099 chars]"
    }
  ]
}
"""

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






  # response = sample_response


  print('url:')
  print(url)

  response_dict = response.json()


  print("Response:")
  print(response)
  print()
  print()
  print(response_dict)


  # ✅ Check for errors
  if response.status_code != 200:
    print("API Error:", response_dict.get("message"))
    return []

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

# print(categories[2], countries['pk'])
running = True

while running:
  try:
    print_options("Available categories", categories)
    category = int(input("Choose 1-5 for category: "))

    print_options("Available countries", countries)
    country = input("Choose one of the country: ")

    news = get_news(country, categories[category - 1])

    for single_news in news:
      print_news(single_news)

    # print(news)
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