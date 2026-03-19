import argparse

parser = argparse.ArgumentParser()

parser.add_argument('command')
parser.add_argument('--file')

args = parser.parse_args()

if args.command == "count":
  with open(args.file, "r") as f:
    content = f.read()
    print(f"The number of words found in the file are {len(content.split())}")