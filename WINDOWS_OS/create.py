#!/usr/bin/python3
import os
from dotenv import load_dotenv
import argparse

# Load the Environment Variable
load_dotenv()

# Argument Parsing
parser = argparse.ArgumentParser(
    description="Default: Simple HTML Boilerplate Project. \n Pass Arguments to change the type"
)
parser.add_argument("name", help="Name of Your Project")
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-n",
    "--nogit",
    help="Git is not Initialised in the Project Folder",
    action="store_true",
)
group.add_argument(
    "-g",
    "--git",
    help="Git is initialised in the Project Folder (Default)",
    action="store_true",
)
parser.add_argument("--version", action="version", version="%(prog)s 1.0")
args = parser.parse_args()

# Get The Data
dir = os.getenv("FILEPATH")
proj_name = args.name
new_dir = os.path.join(dir, proj_name)

# Create and change into the Folder
os.makedirs(new_dir)
os.chdir(new_dir)

commands = [
    "git clone https://github.com/h5bp/html5-boilerplate.git .",
    "rm -rf .git .github README.md CHANGELOG.md",
    "git init",
    "git add .",
    'git commit -m "First Commit" ',
    "code .",
]
ng_commands = [
    "git clone https://github.com/h5bp/html5-boilerplate.git .",
    "rm -rf .git .github README.md CHANGELOG.md",
    "code .",
]
if args.nogit:
    for command in ng_commands:
        os.system(command)
    print("Suscessfully created Project Directory. Git Not Intialised")

else:
    for command in commands:
        os.system(command)
    print("Suscessfully created Project Directory and Git Intialised")


exit()
