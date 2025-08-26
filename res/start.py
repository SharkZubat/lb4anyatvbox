import os
import configparser
import json

config = configparser.ConfigParser()
config.read('res/config.ini')

content = """[Settings]
lang="en"
"""

try:
	lang = config['Settings']['lang']
except:
	print("Error setting language! Creating new \"config.ini\" file...")
	with open('res/config.ini', 'w') as file:
		file.write(content)
	lang = config['Settings']['lang']

with open(f'res/lang/{lang.replace('"', '')}.json', 'r') as f:
	data = json.load(f)

name = data["init"]["nameprogram"]

def printname():
	print(name)
	print("-" * len(name))

def init():
	printname()

init()
