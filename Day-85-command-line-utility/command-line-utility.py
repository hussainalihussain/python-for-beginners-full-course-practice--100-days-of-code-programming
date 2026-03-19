import argparse

# To run this try something like this:
# python command-line-utility.py greet Hussain
# you will get:
# Hello Hussain

parser = argparse.ArgumentParser()

parser.add_argument('command')
parser.add_argument('--name')

args = parser.parse_args()

if args.command == "greet":
  print(f"Hello {args.name}")
