import argparse
import os

'''
Pull and merge the main branch changes from the live/github to the current branch

For this we need these commands:
1. git fetch origin main:main
2. git merge main


How to run it:
python pull-the-latest-changes-of-git.py

if master branch name is "main"
else (let say) if branch name is master then you need to specify it (as this program consider the
default branch name is main):
python pull-the-latest-changes-of-git.py --name=master

'''

parser = argparse.ArgumentParser()

parser.add_argument("-o", "--name", help="Main Branch Name", default="main")

args = parser.parse_args()

main_branch = args.name


command1 = f"git fetch origin {main_branch}:{main_branch}"
command2 = f"git merge {main_branch}"

print("We will run the following commands:")
print(command1)
print(command2)

print()
print("Output of the commands:")

os.system(command1)
os.system(command2)