
import re

email = "see hussainali9616@gmail.com is the email of the user!"

email_pattern = r"([a-zA-Z0-9-_.])+\@[a-zA-Z0-9]+\.(com|net|edu)"

if found:=re.search(email_pattern, email):
  # print (f"Email found:", found)
  found_tuple = found.span()
  # print(found.span()[0], found.span()[1])
  print(f"Founded email in the text: {email[found_tuple[0]:found_tuple[1]]}")


text = '''
Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis cupiditate,
sapiente explicabo debitis dolorem laboriosam beatae officiis repellat eveniet
ratione delectus error obcaecati? Esse repellat dolorum veniam eum,
accusamus possimus.
'''
end_on_us_word_pattern = r" [a-zA-Z]+us[ .]"

matches = re.finditer(end_on_us_word_pattern, text)

for match in matches:
  # print(match.span())
  tuple = match.span()
  # print(tuple[0], tuple[1])
  print(f"Word match: {text[tuple[0]:tuple[1]]}")