#!/usr/bin/python env


import pyperclip as pc
import argparse
import re

# creates a ssh string for git remote repository from original repo link
# https://github.com/<username>/<repo>
# git@github.com:<username>/<repo-name>

def matchLink(link):
    githubLink = "https://github.com/[a-zA-Z0-9]+/[a-zA-Z0-9-_]+"
    # search for a match
    x = re.search(githubLink, link)
    # there is no match for any of the email
    if x == None:
        return False
    # there was a match for the email
    return True


parser = argparse.ArgumentParser(description="Create git remote link for ssh connections")
parser.add_argument("-l", "--link", help="link to remote github repository")
args = vars(parser.parse_args())

link = args['link']

matched = matchLink(link)

if matched:
    splitted = link.split("/")
    # remote ssh connection link/string
    rSSH = f"git@github.com:{splitted[-2]}/{splitted[-1]}"

print(f"Original: {link}")
print(f"SSH String: {rSSH}")
fullCommand = f"git remote add origin {rSSH}"
print(f"Git Remote SHH: {fullCommand}")

# copy to clipboard for copy/paste
pc.copy(fullCommand)
pas = pc.paste()
if pas == fullCommand:
    print("Command Copied to Clipboard..")
else:
    print("There Was an Error..")

