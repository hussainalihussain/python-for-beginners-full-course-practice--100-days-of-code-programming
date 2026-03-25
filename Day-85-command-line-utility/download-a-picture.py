import requests
import argparse

# try to run something like this:
# python download-a-picture.py https://c7.alamy.com/comp/2HWAE9M/success-is-not-random-portrait-of-a-handsome-businessman-leaning-against-a-glass-wall-2HWAE9M.jpg --name=some-picture.jpg
#
# Output will be:
# Downloaded: some-picture.jpg
#
# Note: 

def download_file(url, name):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Save the content to a local file using the 'name' provided
    with open(name, 'wb') as file:
        file.write(response.content)
    
    print(f"Downloaded: {name}")


parser = argparse.ArgumentParser()

parser.add_argument('url')
parser.add_argument("-o", "--name", default="person.png", type=str)

args = parser.parse_args()

download_file(args.url, args.name)
