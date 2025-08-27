import os
import configparser
import json
import keyboard

config = configparser.ConfigParser()
config.read('res/config.ini')

content = """[Settings]
lang="en"
"""

menu="main"

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

def main():
	print(f"(Ctrl+N) {data["project"]["newproj"]}")
	print(f"(Ctrl+O) {data["project"]["opnproj"]}")
	#...input...
	keyboard.add_hotkey('ctrl+n', lambda: print("test success"))

def init():
	printname()
	if menu == "main":
		main()

init()
